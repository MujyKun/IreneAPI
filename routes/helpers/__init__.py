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
    get_all_users,
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

from .channel import add_channel, delete_channel

from .groupmembers import (
    get_person,
    get_persons,
    get_tag,
    get_tags,
    get_date,
    get_dates,
    get_name,
    get_names,
    get_company,
    get_companies,
    get_display,
    get_displays,
    get_locations,
    get_location,
    get_media,
    get_all_media,
    get_person_alias,
    get_person_aliases,
    get_group_aliases,
    get_group_alias,
    get_social,
    get_socials,
    get_position,
    get_positions,
    get_fandoms,
    get_fandom,
    get_affiliation,
    get_affiliations,
    get_blood_type,
    get_blood_types,
)

# Helper Functions for routes.
helper_routes = {
    "company/.GET": {"function": get_companies, "params": ["requestor"]},
    "company/$company_id.GET": {
        "function": get_company,
        "params": ["requestor", "company_id"],
    },
    "display/.GET": {"function": get_displays, "params": ["requestor"]},
    "display/$display_id.GET": {
        "function": get_display,
        "params": ["requestor", "display_id"],
    },
    "location/.GET": {"function": get_locations, "params": ["requestor"]},
    "location/$location_id.GET": {
        "function": get_location,
        "params": ["requestor", "location_id"],
    },
    "media/.GET": {"function": get_all_media, "params": ["requestor"]},
    "media/$name_id.GET": {"function": get_media, "params": ["requestor", "media_id"]},
    "personalias/.GET": {"function": get_person_aliases, "params": ["requestor"]},
    "personalias/$alias_id.GET": {
        "function": get_person_alias,
        "params": ["requestor", "alias_id"],
    },
    "groupalias/.GET": {"function": get_group_aliases, "params": ["requestor"]},
    "groupalias/$alias_id.GET": {
        "function": get_group_alias,
        "params": ["requestor", "alias_id"],
    },
    "social/.GET": {"function": get_socials, "params": ["requestor"]},
    "social/$social_id.GET": {
        "function": get_social,
        "params": ["requestor", "social_id"],
    },
    "position/.GET": {"function": get_positions, "params": ["requestor"]},
    "position/$position_id.GET": {
        "function": get_position,
        "params": ["requestor", "position_id"],
    },
    "fandom/.GET": {"function": get_fandoms, "params": ["requestor"]},
    "fandom/$name_id.GET": {
        "function": get_fandom,
        "params": ["requestor", "guild_id"],
    },
    "affiliation/.GET": {"function": get_affiliations, "params": ["requestor"]},
    "affiliation/$affiliation_id.GET": {
        "function": get_affiliation,
        "params": ["requestor", "affiliation_id"],
    },
    "bloodtype/.GET": {"function": get_blood_types, "params": ["requestor"]},
    "bloodtype/$blood_id.GET": {
        "function": get_blood_type,
        "params": ["requestor", "blood_id"],
    },
    "name/.GET": {"function": get_names, "params": ["requestor"]},
    "name/$name_id.GET": {"function": get_name, "params": ["requestor", "name_id"]},
    "date/.GET": {"function": get_dates, "params": ["requestor"]},
    "date/$date_id.GET": {"function": get_date, "params": ["requestor", "date_id"]},
    "tag/.GET": {"function": get_tags, "params": ["requestor"]},
    "tag/$tag_id.GET": {"function": get_tag, "params": ["requestor", "tag_id"]},
    "person/.GET": {"function": get_persons, "params": ["requestor"]},
    "person/$person_id.GET": {
        "function": get_person,
        "params": ["requestor", "person_id"],
    },
    "user/.GET": {"function": get_all_users, "params": ["requestor"]},
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
    "channel/$channel_id.POST": {
        "function": add_channel,
        "params": ["requestor", "channel_id"],
    },
    "channel/$channel_id.DELETE": {
        "function": delete_channel,
        "params": ["requestor", "channel_id"],
    },
}
