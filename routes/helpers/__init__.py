from passlib.context import CryptContext

# API Tokens are hashed in the DB and should at no point ever be read as plain text.
token_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)


def hash_token(token):
    return token_context.hash(token)


def check_hashed_token(token, hashed):
    return token_context.verify(token, hashed)


from typing import Optional
from models import Requestor, DbConnection
from functools import wraps
from .errors import LackingPermissions


permission_levels = {
    -1: "God",
    0: "Owner",
    1: "Developer",
    2: "Super Patron",
    3: "Friend",
}


def check_permission(permission_level):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Check permission level matches the requirement.
            requestor = kwargs.get("requestor") or args[0]
            if isinstance(requestor, Requestor):
                if requestor.permission_level <= permission_level:
                    # approved access
                    return await func(*args, **kwargs)
            raise LackingPermissions

        return wrapper

    return decorator


db: Optional[DbConnection] = None


class DB:
    def __init__(self):
        self.db: Optional[DbConnection] = None


self = DB()

from .api import add_token, get_token, delete_token, get_permission_level

from .user import (
    get_user_banned,
    ban_user,
    unban_user,
    add_patron,
    get_user_patron,
    add_super_patron,
    add_data_mod,
    add_mod,
    add_proofreader,
    add_translator,
    delete_patron,
    delete_super_patron,
    delete_data_mod,
    delete_mod,
    delete_proofreader,
    delete_translator,
    get_user,
    add_user,
    delete_user,
)

# Helper Functions for routes.
helper_routes = {
    "user/.GET": {"function": get_user, "params": ["requestor", "user_id"]},
    "user/.POST": {"function": add_user, "params": ["requestor", "user_id"]},
    "user/.DELETE": {"function": delete_user, "params": ["requestor", "user_id"]},
    "user/patron_status.GET": {
        "function": get_user_patron,
        "params": ["requestor", "user_id"],
    },
    "user/patron_status.POST": {
        "function": add_patron,
        "params": ["requestor", "user_id"],
    },
    "user/patron_status.DELETE": {
        "function": delete_patron,
        "params": ["requestor", "user_id"],
    },
    "user/ban_status.GET": {
        "function": get_user_banned,
        "params": ["requestor", "user_id"],
    },
    "user/ban_status.POST": {"function": ban_user, "params": ["requestor", "user_id"]},
    "user/ban_status.DELETE": {
        "function": unban_user,
        "params": ["requestor", "user_id"],
    },
}
