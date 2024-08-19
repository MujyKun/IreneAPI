import asyncio

from .helpers import self, get_token, get_permission_level
from typing import Union, Dict
from models import WebSocketSession, Requestor, Access
from .helpers.errors import InvalidLogin, BadRequest
from .helpers import hash_token, check_hashed_token

from quart_openapi import Resource  # used as a general import from blueprint files
from quart import request, make_response, Response
from functools import wraps

from datetime import timedelta
from functools import update_wrapper
from typing import Callable, Iterable, Union

from quart import current_app, make_response, request


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
from .discord import discord

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
    ban_phrases,
    discord
]
