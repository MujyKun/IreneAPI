from .helpers import self, get_token, get_permission_level
from typing import Union, Dict
from models import WebSocketSession, Requestor
from passlib.context import CryptContext
from quart import websocket


# PASS WITH CAUTION. Should only be used in functions not directly returned to a user
# and user authentication is not needed.
god_access_requestor = Requestor(-1, 0)


# API Tokens are hashed in the DB and should at no point ever be read as plain text.
token_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)


def hash_token(token):
    return token_context.hash(token)


def check_hashed_token(token, hashed):
    return token_context.verify(token, hashed)


# connected_websockets defined as { user_id: [WebSocketSessions] }
connected_websockets: Dict[int, Dict[int, WebSocketSession]] = dict()  # A user may have many web socket connections.


async def login(login_headers, handle_websocket=False) -> Union[bool, WebSocketSession]:
    """Log in.

    :param login_headers: Contains the Bearer Auth token and user id.
    :param handle_websocket: Whether a websocket connection needs to be handled.
    """
    error_reason = "Failed to Authenticate."
    error_code = 401
    try:
        token = login_headers['Authorization']
        user_id = int(login_headers['user_id'])
        expected_token = await get_token(requestor=god_access_requestor, user_id=user_id)

        if not expected_token:
            raise Exception("Bad Request")

        login_success = check_hashed_token(token, expected_token)

        if not login_success:
            error_reason += "Token does not match the user."
        else:
            if handle_websocket:
                permission_level = await get_permission_level(god_access_requestor, user_id)
                wss = WebSocketSession(user_id, permission_level)
                existing_ws = connected_websockets.get(user_id)
                if not existing_ws:
                    connected_websockets[user_id] = {wss.wss_id: wss}
                else:
                    existing_ws[wss.wss_id] = wss
                return wss
            return True
    except KeyError:
        error_reason += f"You are missing headers from your request. Please follow the documentation " \
                        f"for login at {'...'}"
    except Exception as e:
        error_code = 400
        error_reason = "Bad Request"

    if handle_websocket:
        await websocket.close(code=error_code, reason=error_reason)
    return False
