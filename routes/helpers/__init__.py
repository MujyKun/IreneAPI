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
from models import Requestor, DbConnection, Access
from functools import wraps
from .errors import LackingPermissions, BadRequest


def is_int64(value: int):
    """Confirm if an integer is in range of int64 to prevent overflow."""
    if -9223372036854775808 > value or value > 9223372036854775807:
        raise BadRequest


# PRE DEFINED ACCESS
GOD = Access(-1)
OWNER = Access(0)
DEVELOPER = Access(1)
SUPER_PATRON = Access(2)
FRIEND = Access(3)
USER = Access(4)


db: Optional[DbConnection] = None


class DB:
    def __init__(self):
        self.db: Optional[DbConnection] = None


self = DB()


async def log(requestor: Requestor, function_name, response, args: str, kwargs: str):
    """Log a user accessing a helper function."""
    try:
        await self.db.execute(
            "SELECT public.logfunc($1, $2, $3, $4, $5)",
            requestor.user_id,
            function_name,
            f"{response}",
            args,
            kwargs,
        )
    except Exception as e:
        print(
            f"Failed to log:\n{e}\n{requestor.user_id}, {function_name} - {response} - {args} - {kwargs}"
        )


def check_permission(permission_level: Access):
    """Decorator to check the permission level of a logged-in user matches the requirement."""

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Check permission level matches the requirement.
            requestor = kwargs.get("requestor") or args[0]

            if isinstance(requestor, Requestor):
                if requestor.access.id <= permission_level.id:
                    # approved access
                    response = await func(*args, **kwargs)
                    # log access
                    try:
                        # we should not log useless args or kwargs,
                        # so they will be removed.
                        if kwargs.get("unhashed_token"):
                            kwargs.pop("unhashed_token")
                        if kwargs.get("requestor"):
                            kwargs.pop("requestor")
                        await log(
                            requestor=requestor,
                            function_name=func.__name__,
                            response=response,
                            args=f"{args}",
                            kwargs=f"{kwargs}",
                        )
                    except Exception as e:
                        print(e)
                    return response
            raise LackingPermissions

        return wrapper

    return decorator


from .api import (
    add_token,
    get_token,
    check_token_exists,
    delete_token,
    get_permission_level,
)

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
    get_user_super_patron,
    get_user_mod,
    get_user_translator,
    get_user_proofreader,
    get_user_data_mod,
)

from .twitter import (
    add_twitter_account,
    delete_twitter_account,
    add_twitter_subscription,
    delete_twitter_subscription,
    get_and_add_twitter_id,
    get_subscriptions,
    get_accounts,
    get_timeline,
)

# Helper Functions for routes.
helper_routes = {
    "user/$user_id.GET": {"function": get_user, "params": ["requestor", "user_id"]},
    "user/$user_id.POST": {"function": add_user, "params": ["requestor", "user_id"]},
    "user/$user_id.DELETE": {
        "function": delete_user,
        "params": ["requestor", "user_id"],
    },
    "user/patron_status/$user_id.GET": {
        "function": get_user_patron,
        "params": ["requestor", "user_id"],
    },
    "user/patron_status/$user_id.POST": {
        "function": add_patron,
        "params": ["requestor", "user_id"],
    },
    "user/patron_status/$user_id.DELETE": {
        "function": delete_patron,
        "params": ["requestor", "user_id"],
    },
    "user/ban_status/$user_id.GET": {
        "function": get_user_banned,
        "params": ["requestor", "user_id"],
    },
    "user/ban_status/$user_id.POST": {
        "function": ban_user,
        "params": ["requestor", "user_id"],
    },
    "user/ban_status/$user_id.DELETE": {
        "function": unban_user,
        "params": ["requestor", "user_id"],
    },
    "user/token/$user_id.GET": {
        "function": check_token_exists,
        "params": ["requestor", "user_id"],
    },
    "user/token/$user_id.POST": {
        "function": add_token,
        "params": ["requestor", "user_id", "unhashed_token", "access_id"],
    },
    "user/token/$user_id.DELETE": {
        "function": delete_token,
        "params": ["requestor", "user_id"],
    },
    "user/superpatron_status/$user_id.GET": {
        "function": get_user_super_patron,
        "params": ["requestor", "user_id"],
    },
    "user/superpatron_status/$user_id.POST": {
        "function": add_super_patron,
        "params": ["requestor", "user_id"],
    },
    "user/superpatron_status/$user_id.DELETE": {
        "function": delete_super_patron,
        "params": ["requestor", "user_id"],
    },
    "user/mod_status/$user_id.GET": {
        "function": get_user_mod,
        "params": ["requestor", "user_id"],
    },
    "user/mod_status/$user_id.POST": {
        "function": add_mod,
        "params": ["requestor", "user_id"],
    },
    "user/mod_status/$user_id.DELETE": {
        "function": delete_mod,
        "params": ["requestor", "user_id"],
    },
    "user/data_mod_status/$user_id.GET": {
        "function": get_user_data_mod,
        "params": ["requestor", "user_id"],
    },
    "user/data_mod_status/$user_id.POST": {
        "function": add_data_mod,
        "params": ["requestor", "user_id"],
    },
    "user/data_mod_status/$user_id.DELETE": {
        "function": delete_data_mod,
        "params": ["requestor", "user_id"],
    },
    "user/translator_status/$user_id.GET": {
        "function": get_user_translator,
        "params": ["requestor", "user_id"],
    },
    "user/translator_status/$user_id.POST": {
        "function": add_translator,
        "params": ["requestor", "user_id"],
    },
    "user/translator_status/$user_id.DELETE": {
        "function": delete_translator,
        "params": ["requestor", "user_id"],
    },
    "user/proofreader_status/$user_id.GET": {
        "function": get_user_proofreader,
        "params": ["requestor", "user_id"],
    },
    "user/proofreader_status/$user_id.POST": {
        "function": add_proofreader,
        "params": ["requestor", "user_id"],
    },
    "user/proofreader_status/$user_id.DELETE": {
        "function": delete_proofreader,
        "params": ["requestor", "user_id"],
    },
    "twitter/$twitter_id/$channel_id.GET": {
        "function": twitter.is_subscribed,
        "params": ["requestor", "twitter_id", "channel_id"],
    },
    "twitter/$twitter_id/$channel_id.POST": {
        "function": add_twitter_subscription,
        "params": ["requestor", "account_id", "channel_id"],
        "optional": ["role_id"],
    },
    "twitter/$twitter_id/$channel_id.DELETE": {
        "function": delete_twitter_subscription,
        "params": ["requestor", "account_id", "channel_id"],
    },
    "twitter/$twitter_info.GET": {
        "function": get_subscriptions,
        "params": ["requestor", "twitter_info"],
    },  # twitter_info can be a twitter id or Twitter username.
    "twitter/$twitter_info.POST": {
        "function": get_and_add_twitter_id,
        "params": ["requestor", "username"],
    },
    "twitter/$twitter_info.DELETE": {
        "function": delete_twitter_account,
        "params": ["requestor", "account_id"],
    },
    "twitter/subscriptions.GET": {
        "function": get_subscriptions,
        "params": ["requestor"],
    },
    "twitter/accounts.GET": {
        "function": get_accounts,
        "params": ["requestor"],
    },
    "twitter/timeline/$twitter_id.GET": {
        "function": get_timeline,
        "params": ["requestor", "twitter_id"],
    },
}
