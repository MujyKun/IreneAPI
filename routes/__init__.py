from .helpers import self, get_token, get_permission_level
from typing import Union, Dict
from models import WebSocketSession, Requestor, Access
from .helpers.errors import InvalidLogin, BadRequest
from .helpers import hash_token, check_hashed_token


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
            raise BadRequest

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
        raise BadRequest

    # if handle_websocket:
    # await websocket.close(code=error_code, reason=error_reason)
    raise InvalidLogin
