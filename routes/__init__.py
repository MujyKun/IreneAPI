import asyncio

from .helpers import self, get_token, get_permission_level
from typing import Union, Dict
from models import WebSocketSession, Requestor, Access
from .helpers.errors import InvalidLogin, BadRequest
from .helpers import hash_token, check_hashed_token

from quart_openapi import Resource as NoCorsResource
from quart import request, make_response, Response
from functools import wraps

from datetime import timedelta
from functools import update_wrapper
from typing import Callable, Iterable, Union

from quart import current_app, make_response, request


# pylint: disable=too-many-arguments
def crossdomain(
    origin: str = None,
    methods: Iterable[str] = None,
    headers: Union[str, Iterable[str]] = None,
    expose_headers: Union[str, Iterable[str]] = None,
    max_age: Union[int, timedelta] = 21600,
    attach_to_all: bool = True,
    automatic_options: bool = True,
    credentials: bool = False,
) -> Callable:
    """Decorator for `CORS <https://fetch.spec.whatwg.org/#http-cors-protocol>`_ adapted from
    http://flask.pocoo.org/snippets/56/

    Irene Implementation. Original Implementation found in `from quart_openapi.cors import crossdomain`

    :param origin: value for `Access-Control-Allow-Origin` header
    :param methods: str or list[str] of HTTP verbs for the `Access-Control-Allow-Methods`, defaults
                    to 'OPTIONS, HEAD' + any available verb functions on the class
    :param headers: str or list[str] for the `Access-Control-Allow-Headers` header
    :param expose_headers: str or list[str] for the `Access-Control-Expose-Headers` header
    :param max_age: the number of seconds for the `Access-Control-Max-Age` header.
    :param attach_to_all: if `False`, the CORS headers will only be attached to `OPTIONS` requests
    :param automatic_options: if `False`, will look for an options function in the resource, otherwise
                              the default options response will be used for OPTIONS requests,
                              and the CORS headers will be attached
    :param credentials: the value of the `Access-Control-Allow-Credentials` header

    This decorator should be used on individual route functions like so:

    .. code-block:: python

          @app.route('/foobar', methods=['GET','OPTIONS'])
          class CORS(Resource):
            @crossdomain(origin='*')
            async def get(self):
              ...

    This would allow Cross Origin requests to make get requests to '/foobar'.
    """
    if methods is not None:
        methods = ", ".join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ", ".join(x.upper() for x in headers)
    if expose_headers is not None and not isinstance(expose_headers, str):
        expose_headers = ", ".join(x.upper() for x in expose_headers)
    if not isinstance(origin, str):
        origin = ", ".join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def decorator(func):
        async def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == "OPTIONS":
                resp = await current_app.make_default_options_response()
            else:
                resp = await make_response(await func(*args, **kwargs))
            if not attach_to_all and request.method != "OPTIONS":
                return resp

            hdrs = resp.headers

            hdrs["Access-Control-Allow-Origin"] = origin
            hdrs["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            hdrs["Access-Control-Max-Age"] = str(max_age)
            if credentials:
                hdrs["Access-Control-Allow-Credentials"] = "true"
            if headers is not None:
                hdrs["Access-Control-Allow-Headers"] = headers
            if expose_headers is not None:
                hdrs["Access-Control-Expose-Headers"] = expose_headers
            return resp

        func.provide_automatic_options = False
        return update_wrapper(wrapped_function, func)

    return decorator


async def cors_handler(func):
    @wraps(func)
    @crossdomain(origin="*", headers="authorization")
    async def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            return func(*args, **kwargs)

    return wrapper


class Resource(NoCorsResource):
    def __init__(self, *args, **kwargs):
        super(NoCorsResource, self).__init__()

    async def dispatch_request(self, *args, **kwargs):
        """Add Cors to each type of request in the resource."""
        handler = await cors_handler(getattr(self, request.method.lower(), None))
        if handler is None and request.method == "HEAD" or request.method == "OPTIONS":
            handler = getattr(self, "get", None)
        await self.validate_payload(handler)
        return await handler(*args, **kwargs)


# PASS WITH CAUTION. Should only be used in functions not directly returned to a user
# and user authentication is not needed.
god_access_requestor = Requestor(-1, Access(-1))

# connected_websockets defined as { user_id: [WebSocketSessions] }
connected_websockets: Dict[
    int, Dict[int, WebSocketSession]
] = dict()  # A user may have many web socket connections.


async def login(
    headers, data, handle_websocket=False
) -> Union[WebSocketSession, Requestor]:
    """Log in.

    :param headers: Contains the Bearer Auth token and user id.
    :param data: Form data (should contain the login user id)
    :param handle_websocket: Whether a websocket connection needs to be handled.
    """
    try:
        token = headers["Authorization"]
        user_id = int(data["user_id"])
        expected_token = (
            await get_token(requestor=god_access_requestor, user_id=user_id)
        )["results"]["gettoken"]
        if not expected_token:
            raise BadRequest(None, "No token was found for your user.")

        login_success = check_hashed_token(token.replace("Bearer ", ""), expected_token)

        if login_success:
            permission_level = (
                await get_permission_level(god_access_requestor, user_id)
            )["results"]["getaccessid"]

            if handle_websocket:
                wss = WebSocketSession(user_id, Access(permission_level))
                existing_ws = connected_websockets.get(user_id)
                if not existing_ws:
                    connected_websockets[user_id] = {wss.wss_id: wss}
                else:
                    existing_ws[wss.wss_id] = wss
                return wss
            return Requestor(user_id, Access(permission_level))
    except Exception as e:
        raise BadRequest(None, e)

    # if handle_websocket:
    # await websocket.close(code=error_code, reason=error_reason)
    raise InvalidLogin


from .affiliation import affiliation
from .company import company
from .display import display
from .fandom import fandom
from .group import group
from .groupalias import groupalias
from .guild import guild
from .location import location
from .media import media
from .name import name
from .person import person
from .personalias import personalias
from .position import position
from .social import social
from .tag import tag
from .channel import channel
from .userstatus import status as user_status
from .user import user
from .guessinggame import gg as guessinggame
from .unscramblegame import us as unscramblegame
from .twitch import twitch
from .biasgame import biasgame
from .wolfram import wolfram
from .eightball import eight_ball
from .notifications import noti
from .interactions import interactions as interactions_blueprint
from .misc import misc
from .reminders import reminders as reminders_blueprint
from .bot import bot
from .tiktok import tiktok
from .banphrases import ban_phrases

blueprints = [
    affiliation,
    company,
    display,
    fandom,
    group,
    groupalias,
    guild,
    location,
    media,
    name,
    person,
    personalias,
    position,
    social,
    tag,
    channel,
    user,
    guessinggame,
    user_status,
    twitch,
    unscramblegame,
    wolfram,
    biasgame,
    eight_ball,
    noti,
    interactions_blueprint,
    misc,
    reminders_blueprint,
    bot,
    tiktok,
    ban_phrases
]
