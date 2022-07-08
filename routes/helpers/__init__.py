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
    if value is None or (-9223372036854775808 > value or value > 9223372036854775807):
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
    toggle_gg_filter,
    upsert_gg_filter_groups,
    upsert_gg_filter_persons,
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

from .channel import add_channel, delete_channel, get_channel, get_channels

from .groupmembers import (
    get_person,
    get_persons,
    get_group,
    get_groups,
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
    get_fandoms_by_group,
    get_affiliation,
    get_affiliations,
    get_blood_type,
    get_blood_types,
    add_company,
    add_display,
    add_location,
    delete_person,
    delete_group,
    delete_company,
    delete_display,
    delete_location,
    add_media,
    add_group,
    add_person,
    add_person_alias,
    add_group_alias,
    add_social,
    delete_social,
    delete_group_alias,
    delete_person_alias,
    delete_media,
    add_position,
    delete_position,
    add_fandom,
    delete_fandom,
    delete_affiliation,
    add_affiliation,
    add_blood_type,
    delete_blood_type,
    add_name,
    delete_name,
    add_date,
    update_date,
    delete_date,
    add_tag,
    delete_tag,
    get_person_media_info,
    get_group_media_info,
    get_affiliation_media_info,
    generate_media_group,
    generate_media_person,
    generate_media_affiliation,
    upsert_media_difficulty,
)

from .guessinggame import add_gg, delete_gg, get_gg, get_all_ggs

from .guild import get_guild, get_guilds, add_guild, delete_guild

# Helper Functions for routes.

helper_routes = {
    "guessinggame/$gg_id.GET": {"function": get_gg, "params": ["requestor", "game_id"]},
    "guessinggame/$gg_id.DELETE": {
        "function": delete_gg,
        "params": ["requestor", "game_id"],
    },
    "guessinggame/.GET": {"function": get_all_ggs, "params": ["requestor"]},
    "guessinggame/.POST": {
        "function": add_gg,
        "params": [
            "requestor",
            "date_id",
            "media_ids",
            "status_ids",
            "mode_id",
            "difficulty_id",
            "is_nsfw",
        ],
    },
    "guild/.GET": {"function": get_guilds, "params": ["requestor"]},
    "guild/$guild_id.GET": {
        "function": get_guild,
        "params": ["requestor", "guild_id"],
    },
    "guild/.POST": {
        "function": add_guild,
        "params": [
            "requestor",
            "guild_id",
            "name",
            "emoji_count",
            "region",
            "afk_timeout",
            "icon",
            "owner_id",
            "banner",
            "description",
            "mfa_level",
            "splash",
            "nitro_level",
            "boosts",
            "text_channel_count",
            "voice_channel_count",
            "category_count",
            "emoji_limit",
            "member_count",
            "role_count",
            "shard_id",
            "create_date",
            "has_bot",
        ],
    },
    "guild/$guild_id.DELETE": {
        "function": delete_guild,
        "params": ["requestor", "guild_id"],
    },
    "company/.GET": {"function": get_companies, "params": ["requestor"]},
    "company/$company_id.GET": {
        "function": get_company,
        "params": ["requestor", "company_id"],
    },
    "company/.POST": {
        "function": add_company,
        "params": ["requestor", "name", "description", "date_id"],
    },
    "company/$company_id.DELETE": {
        "function": delete_company,
        "params": ["requestor", "company_id"],
    },
    "display/.GET": {"function": get_displays, "params": ["requestor"]},
    "display/$display_id.GET": {
        "function": get_display,
        "params": ["requestor", "display_id"],
    },
    "display/.POST": {
        "function": add_display,
        "params": ["requestor", "avatar", "banner"],
    },
    "display/$display_id.DELETE": {
        "function": delete_display,
        "params": ["requestor", "display_id"],
    },
    "location/.GET": {"function": get_locations, "params": ["requestor"]},
    "location/$location_id.GET": {
        "function": get_location,
        "params": ["requestor", "location_id"],
    },
    "location/.POST": {
        "function": add_location,
        "params": ["requestor", "country", "city"],
    },
    "location/$location_id.DELETE": {
        "function": delete_location,
        "params": ["requestor", "location_id"],
    },
    "media/.GET": {"function": get_all_media, "params": ["requestor"]},
    "media/.POST": {
        "function": add_media,
        "params": [
            "requestor",
            "link",
            "faces",
            "file_type",
            "affiliation_id",
            "enabled",
            "is_nsfw",
        ],
    },
    "media/$media_id.GET": {"function": get_media, "params": ["requestor", "media_id"]},
    "media/$media_id.DELETE": {
        "function": get_media,
        "params": ["requestor", "media_id"],
    },
    "media/$media_id.POST": {
        "function": upsert_media_difficulty,
        "params": ["requestor", "media_id", "failed_guesses", "correct_guesses"],
    },
    "personalias/.GET": {"function": get_person_aliases, "params": ["requestor"]},
    "personalias/$alias_id.GET": {
        "function": get_person_alias,
        "params": ["requestor", "alias_id"],
    },
    "personalias/$alias_id.DELETE": {
        "function": delete_person_alias,
        "params": ["requestor", "alias_id"],
    },
    "personalias/.POST": {
        "function": add_person_alias,
        "params": ["requestor", "alias", "person_id"],
        "optional": ["guild_id"],
    },
    "groupalias/.GET": {"function": get_group_aliases, "params": ["requestor"]},
    "groupalias/$alias_id.GET": {
        "function": get_group_alias,
        "params": ["requestor", "alias_id"],
    },
    "groupalias/$alias_id.DELETE": {
        "function": delete_group_alias,
        "params": ["requestor", "alias_id"],
    },
    "groupalias/.POST": {
        "function": add_group_alias,
        "params": ["requestor", "alias", "group_id"],
        "optional": ["guild_id"],
    },
    "social/.GET": {"function": get_socials, "params": ["requestor"]},
    "social/.POST": {
        "function": add_social,
        "params": [
            "requestor",
            "twitter",
            "youtube",
            "melon",
            "instagram",
            "vlive",
            "spotify",
            "fancafe",
            "facebook",
            "tiktok",
        ],
    },
    "social/$social_id.GET": {
        "function": get_social,
        "params": ["requestor", "social_id"],
    },
    "social/$social_id.DELETE": {
        "function": delete_social,
        "params": ["requestor", "social_id"],
    },
    "position/.GET": {"function": get_positions, "params": ["requestor"]},
    "position/.POST": {
        "function": add_position,
        "params": ["requestor", "position_name"],
    },
    "position/$position_id.GET": {
        "function": get_position,
        "params": ["requestor", "position_id"],
    },
    "position/$position_id.DELETE": {
        "function": delete_position,
        "params": ["requestor", "position_id"],
    },
    "fandom/.GET": {"function": get_fandoms, "params": ["requestor"]},
    "fandom/$group_id.DELETE": {
        "function": delete_fandom,
        "params": ["requestor", "group_id", "fandom_name"],
    },
    "fandom/$group_id.POST": {
        "function": add_fandom,
        "params": ["requestor", "group_id", "fandom_name"],
    },
    "fandom/$group_id.GET": {
        "function": get_fandoms_by_group,
        "params": ["requestor", "group_id"],
    },
    "affiliation/$affiliation_id/media.GET": {
        "function": get_affiliation_media_info,
        "params": ["requestor", "affiliation_id"],
    },
    "affiliation/$affiliation_id/media.POST": {
        "function": generate_media_affiliation,
        "params": ["requestor", "affiliation_id"],
        "optional": ["min_faces", "max_faces", "file_type", "nsfw", "enabled"],
    },
    "affiliation/.GET": {"function": get_affiliations, "params": ["requestor"]},
    "affiliation/.POST": {
        "function": add_affiliation,
        "params": ["requestor", "person_id", "group_id", "position_ids", "stage_name"],
    },
    "affiliation/$affiliation_id.GET": {
        "function": get_affiliation,
        "params": ["requestor", "affiliation_id"],
    },
    "affiliation/$affiliation_id.DELETE": {
        "function": delete_affiliation,
        "params": ["requestor", "affiliation_id"],
    },
    "bloodtype/.GET": {"function": get_blood_types, "params": ["requestor"]},
    "bloodtype/.POST": {"function": add_blood_type, "params": ["requestor", "name"]},
    "bloodtype/$blood_id.GET": {
        "function": get_blood_type,
        "params": ["requestor", "blood_id"],
    },
    "bloodtype/$blood_id.DELETE": {
        "function": delete_blood_type,
        "params": ["requestor", "blood_id"],
    },
    "name/.GET": {"function": get_names, "params": ["requestor"]},
    "name/.POST": {
        "function": add_name,
        "params": ["requestor", "first_name", "last_name"],
    },
    "name/$name_id.GET": {"function": get_name, "params": ["requestor", "name_id"]},
    "name/$name_id.DELETE": {
        "function": delete_name,
        "params": ["requestor", "name_id"],
    },
    "date/.GET": {"function": get_dates, "params": ["requestor"]},
    "date/.POST": {
        "function": add_date,
        "params": ["requestor", "start_date", "end_date"],
    },
    "date/$date_id.GET": {"function": get_date, "params": ["requestor", "date_id"]},
    "date/$date_id.PUT": {
        "function": update_date,
        "params": ["requestor", "date_id", "end_date"],
    },
    "date/$date_id.DELETE": {
        "function": delete_date,
        "params": ["requestor", "date_id"],
    },
    "tag/.GET": {"function": get_tags, "params": ["requestor"]},
    "tag/.POST": {"function": add_tag, "params": ["requestor", "name"]},
    "tag/$tag_id.GET": {"function": get_tag, "params": ["requestor", "tag_id"]},
    "tag/$tag_id.DELETE": {"function": delete_tag, "params": ["requestor", "tag_id"]},
    "person/$person_id/media.GET": {
        "function": get_person_media_info,
        "params": ["requestor", "person_id"],
    },
    "person/$person_id/media.POST": {
        "function": generate_media_person,
        "params": ["requestor", "person_id"],
        "optional": ["min_faces", "max_faces", "file_type", "nsfw", "enabled"],
    },
    "person/.GET": {"function": get_persons, "params": ["requestor"]},
    "person/.POST": {
        "function": add_person,
        "params": [
            "requestor",
            "date_id",
            "name_id",
            "former_name_id",
            "gender",
            "description",
            "height",
            "display_id",
            "social_id",
            "location_id",
            "tag_ids",
            "blood_id",
            "call_count",
        ],
    },
    "person/$person_id.GET": {
        "function": get_person,
        "params": ["requestor", "person_id"],
    },
    "person/$person_id.DELETE": {
        "function": delete_person,
        "params": ["requestor", "person_id"],
    },
    "group/$group_id/media.GET": {
        "function": get_group_media_info,
        "params": ["requestor", "group_id"],
    },
    "group/$group_id/media.POST": {
        "function": generate_media_group,
        "params": ["requestor", "group_id"],
        "optional": ["min_faces", "max_faces", "file_type", "nsfw", "enabled"],
    },
    "group/.GET": {"function": get_groups, "params": ["requestor"]},
    "group/.POST": {
        "function": add_group,
        "params": [
            "requestor",
            "group_name",
            "date_id",
            "description",
            "company_id",
            "display_id",
            "website",
            "social_id",
            "tag_ids",
        ],
    },
    "group/$group_id.GET": {
        "function": get_group,
        "params": ["requestor", "group_id"],
    },
    "group/$group_id.DELETE": {
        "function": delete_group,
        "params": ["requestor", "group_id"],
    },
    "user/.GET": {"function": get_all_users, "params": ["requestor"]},
    "user/toggleggfilter/$user_id.POST": {
        "function": toggle_gg_filter,
        "params": ["requestor", "user_id", "active"],
    },
    "user/ggfilterpersons/$user_id.POST": {
        "function": upsert_gg_filter_persons,
        "params": ["requestor", "user_id", "person_ids"],
    },
    "user/ggfiltergroups/$user_id.POST": {
        "function": upsert_gg_filter_groups,
        "params": ["requestor", "user_id", "group_ids"],
    },
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
    "channel/.GET": {
        "function": get_channels,
        "params": ["requestor"],
    },
    "channel/$channel_id.GET": {
        "function": get_channel,
        "params": ["requestor", "channel_id"],
    },
    "channel/.POST": {
        "function": add_channel,
        "params": ["requestor", "channel_id"],
    },
    "channel/$channel_id.DELETE": {
        "function": delete_channel,
        "params": ["requestor", "channel_id"],
    },
}
