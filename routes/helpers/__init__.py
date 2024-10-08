from secrets import token_urlsafe
from concurrent import futures
from passlib.context import CryptContext
from cryptography.fernet import Fernet
from typing import Optional

# API Tokens are hashed in the DB and should at no point ever be read as plain text.
token_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)

COMMANDS_FILE_NAME = "commands.json"


def generate_cookie():
    """Generate a url-safe cookie."""
    return token_urlsafe(32)


cipher_suite = None


def get_cipher_suite() -> Fernet:
    """
    Get the cipher suite.

    Intentionally designed this way to prevent issues with event loop not being initialized on import.
    """
    global cipher_suite
    if not cipher_suite:
        from resources.keys import encryption_key
        cipher_suite = Fernet(encryption_key)
    return cipher_suite


def encrypt_data(data: str) -> Optional[str]:
    """Encrypt Data"""
    if not data:
        return None

    data_bytes = data.encode('utf-8')

    encrypted_data = get_cipher_suite().encrypt(data_bytes)
    return encrypted_data.decode('utf-8')


def decrypt_data(data: str) -> Optional[str]:
    """Decrypt encrypted data."""
    if not data:
        return None

    encrypted_data_bytes = data.encode('utf-8')
    decrypted_data = get_cipher_suite().decrypt(encrypted_data_bytes)
    return decrypted_data.decode('utf-8')


def hash_token(token):
    return token_context.hash(token)


def check_hashed_token(token, hashed):
    return token_context.verify(token, hashed)


from models import Requestor, DbConnection, Access
from functools import wraps
from .errors import LackingPermissions, BadRequest
from datetime import date, datetime

COMMON_TIMESTAMP_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'
COMMON_DATE_FORMAT = "%Y-%m-%d"


def convert_to_timestamp(date_string: str) -> Optional[datetime]:
    """
    Convert a string to a timestamp.

    :param date_string: str
    :return: Optional[date]
    """
    return datetime.strptime(date_string, COMMON_TIMESTAMP_FORMAT) if date_string else None


def convert_to_date(date_string: str) -> Optional[date]:
    """
    Convert a string to a date.

    :param date_string: str
    :return: Optional[date]
    """
    return datetime.strptime(date_string, COMMON_DATE_FORMAT) if date_string else None


def is_int64(value: int):
    """Confirm if an integer is in range of int64 to prevent overflow."""
    if value is None or (-9223372036854775808 > value or value > 9223372036854775807):
        raise BadRequest(None, f"{value} is not int64 or is NoneType.")


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
                    callback_id = kwargs.get("callback_id")
                    if callback_id:
                        kwargs.pop("callback_id")

                    response = await func(*args, **kwargs)
                    # log access
                    try:
                        # we should not log useless args or kwargs,
                        # so they will be removed.
                        if kwargs.get("unhashed_token"):
                            kwargs.pop("unhashed_token")
                        if kwargs.get("requestor"):
                            kwargs.pop("requestor")
                        if callback_id:
                            kwargs["callback_id"] = callback_id
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


thread_pool = futures.ThreadPoolExecutor(max_workers=10)

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

from .channel import add_channel, delete_channel, get_channel, get_channels

from .groupmembers import (
    get_person,
    get_persons,
    get_group,
    get_groups,
    get_tag,
    get_tags,
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
    get_media_by_affiliations,
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
    add_name,
    delete_name,
    add_tag,
    delete_tag,
    get_person_media_info,
    get_group_media_info,
    get_affiliation_media_info,
    generate_media_group,
    generate_media_person,
    generate_media_affiliation,
    get_image_host_url,
    upsert_media_difficulty,
    add_auto_media,
    remove_auto_media,
    get_auto_media,
)

from .userstatus import (
    update_status,
    delete_status,
    get_status,
    get_statuses,
    add_status,
)

from .guessinggame import (
    update_gg_end_time,
    add_gg,
    delete_gg,
    get_gg,
    get_all_ggs,
    update_media_and_status,
)
from .unscramblegame import (
    update_us_end_time,
    add_us,
    delete_us,
    get_us,
    get_all_uss,
    update_status as update_us_status,
)

from .guild import (
    get_guild,
    get_guilds,
    add_guild,
    delete_guild,
    add_prefix,
    delete_prefix,
    get_prefixes,
    get_all_prefixes,
)

from .twitch import (
    get_twitch_channels,
    get_twitch_channel,
    update_posted,
    unsubscribe_from_twitch_channel,
    subscribe_to_twitch_channel,
    get_twitch_channels_by_guild,
    is_live as is_twitch_live,
    username_exists as twitch_acc_exists,
    get_posted,
)

from .wolfram import wolfram_query

from .language import get_languages
from .biasgame import generate_pvp, generate_bracket, get_winners, upsert_wins

from .eightball import get_responses, get_response, add_response, delete_response

from .notifications import get_noti, get_notifications, delete_noti, add_notification
from .interactions import (
    get_interactions,
    add_interaction,
    add_interaction_type,
    delete_interaction,
    delete_interaction_type,
)

from .reminders import add_reminder, delete_reminder, get_reminders

from .reactionroles import add_reaction_role_message, get_reaction_role_messages
from .misc import get_urban_definitions

from .bot import update_commands, get_commands, update_stats

from .tiktok import get_tiktok_accounts, get_latest_tiktok_video, add_tiktok_account, get_tiktok_account, \
    delete_tiktok_account

from .banphrases import get_ban_phrase, add_ban_phrase, delete_ban_phrase, get_ban_phrases

# Helper Functions for routes.


helper_routes = {
    "banphrases/$phrase_id.GET": {"function": get_ban_phrase, "params": ["requestor", "phrase_id"]},
    "banphrases/$phrase_id.DELETE": {"function": delete_ban_phrase, "params": ["requestor", "phrase_id"]},
    "banphrases/.GET": {"function": get_ban_phrases, "params": ["requestor"]},
    "banphrases/.POST": {"function": add_ban_phrase, "params": ["requestor", "guild_id", "log_channel_id", "phrase",
                                                                "punishment"]},
    "tiktok/$username.DELETE": {"function": delete_tiktok_account, "params": ["requestor", "username", "channel_id"]},
    "tiktok/$username.GET": {"function": get_tiktok_account, "params": ["requestor", "username"]},
    "tiktok/.POST": {
        "function": add_tiktok_account,
        "params": ["requestor", "username", "user_id", "channel_id"],
        "optional": ["role_id"],
    },
    "tiktok/.GET": {"function": get_tiktok_accounts, "params": ["requestor"]},
    "tiktok/latest_video/$username.GET": {
        "function": get_latest_tiktok_video,
        "params": ["requestor", "username"],
    },
    "bot/updatestats.PUT": {
        "function": update_stats,
        "params": ["requestor", "key", "value"],
    },
    "bot/commands.PUT": {
        "function": update_commands,
        "params": ["requestor", "commands"],
    },
    "bot/commands.GET": {"function": get_commands, "params": ["requestor"]},
    "reaction_roles/$message_id.POST": {
        "function": add_reaction_role_message,
        "params": ["requestor", "message_id"],
    },
    "reaction_roles/.GET": {
        "function": get_reaction_role_messages,
        "params": ["requestor"],
    },
    "reminder/$remind_id.DELETE": {
        "function": delete_reminder,
        "params": ["requestor", "remind_id"],
    },
    "reminder/.POST": {
        "function": add_reminder,
        "params": ["requestor", "user_id", "reason", "notify_date"],
    },
    "reminder/.GET": {"function": get_reminders, "params": ["requestor"]},
    "affiliation/automedia.GET": {"function": get_auto_media, "params": ["requestor"]},
    "affiliation/automedia.POST": {
        "function": add_auto_media,
        "params": ["requestor", "channel_id", "affiliation_id", "hours_after"],
    },
    "affiliation/automedia.DELETE": {
        "function": remove_auto_media,
        "params": ["requestor", "channel_id", "affiliation_id"],
    },
    "misc/urban.POST": {
        "function": get_urban_definitions,
        "params": ["requestor", "phrase"],
    },
    "interactions/.GET": {"function": get_interactions, "params": ["requestor"]},
    "interactions/.POST": {
        "function": add_interaction,
        "params": ["requestor", "type_id", "url"],
    },
    "interactions/.DELETE": {
        "function": delete_interaction,
        "params": ["requestor", "type_id", "url"],
    },
    "interactions/type.POST": {
        "function": add_interaction_type,
        "params": ["requestor", "name"],
    },
    "interactions/type.DELETE": {
        "function": delete_interaction_type,
        "params": ["requestor", "type_id"],
    },
    "noti/$noti_id.GET": {"function": get_noti, "params": ["requestor", "noti_id"]},
    "noti/$noti_id.DELETE": {
        "function": delete_noti,
        "params": ["requestor", "noti_id"],
    },
    "noti/.GET": {"function": get_notifications, "params": ["requestor"]},
    "noti/.POST": {
        "function": add_notification,
        "params": ["requestor", "guild_id", "user_id", "phrase"],
    },
    "8ball/$response_id.GET": {
        "function": get_response,
        "params": ["requestor", "response_id"],
    },
    "8ball/$response_id.DELETE": {
        "function": delete_response,
        "params": ["requestor", "response_id"],
    },
    "8ball/.GET": {
        "function": get_responses,
        "params": ["requestor"],
    },
    "8ball/.POST": {
        "function": add_response,
        "params": ["requestor", "response"],
    },
    "media/download/$media_id.GET": {
        "function": get_image_host_url,
        "params": ["requestor", "media_id"],
    },
    "biasgame/winners.PUT": {
        "function": upsert_wins,
        "params": ["requestor", "user_id", "person_id"],
    },
    "biasgame/winners.POST": {
        "function": get_winners,
        "params": ["requestor", "user_id"],
        "optional": ["limit"],
    },
    "biasgame/generate_bracket.POST": {
        "function": generate_bracket,
        "params": ["requestor", "game_info"],
    },
    "biasgame/generate_pvp.POST": {
        "function": generate_pvp,
        "params": ["requestor", "first_image_url", "second_image_url"],
    },
    "wolfram/.POST": {"function": wolfram_query, "params": ["requestor", "query"]},
    "language/.GET": {"function": get_languages, "params": ["requestor"]},
    "guild/prefix/.GET": {"function": get_all_prefixes, "params": ["requestor"]},
    "guild/prefix/$guild_id.GET": {
        "function": get_prefixes,
        "params": ["requestor", "guild_id", "prefix"],
    },
    "guild/prefix/$guild_id.POST": {
        "function": add_prefix,
        "params": ["requestor", "guild_id", "prefix"],
    },
    "guild/prefix/$guild_id.DELETE": {
        "function": delete_prefix,
        "params": ["requestor", "guild_id", "prefix"],
    },
    "twitch/already_posted/$username.GET": {
        "function": get_posted,
        "params": ["requestor", "username"],
    },
    "twitch/exists/$username.GET": {
        "function": twitch_acc_exists,
        "params": ["requestor", "username"],
    },
    "twitch/is_live.GET": {
        "function": is_twitch_live,
        "params": ["requestor", "usernames"],
    },
    "twitch/filter/$guild_id.GET": {
        "function": get_twitch_channels_by_guild,
        "params": ["requestor", "guild_id"],
    },
    "twitch/$username.GET": {
        "function": get_twitch_channel,
        "params": ["requestor", "username"],
    },
    "twitch/$username.POST": {
        "function": subscribe_to_twitch_channel,
        "params": ["requestor", "username", "channel_id"],
        "optional": ["role_id"],
    },
    "twitch/$username.DELETE": {
        "function": unsubscribe_from_twitch_channel,
        "params": ["requestor", "username", "channel_id"],
    },
    "twitch/$username.PUT": {
        "function": update_posted,
        "params": ["requestor", "username", "channel_ids", "posted"],
    },
    "twitch/.GET": {"function": get_twitch_channels, "params": ["requestor"]},
    "unscramblegame/$us_id.GET": {
        "function": get_us,
        "params": ["requestor", "game_id"],
    },
    "unscramblegame/$us_id.PUT": {
        "function": update_us_status,
        "params": ["requestor", "game_id", "status_ids"],
    },
    "unscramblegame/$us_id.POST": {
        "function": update_us_end_time,
        "params": ["requestor", "game_id", "end_time"],
    },
    "unscramblegame/$us_id.DELETE": {
        "function": delete_us,
        "params": ["requestor", "game_id"],
    },
    "unscramblegame/.GET": {"function": get_all_uss, "params": ["requestor"]},
    "unscramblegame/.POST": {
        "function": add_us,
        "params": [
            "requestor",
            "start_date",
            "status_ids",
            "mode_id",
            "difficulty_id",
        ],
    },
    "user_status/.GET": {"function": get_statuses, "params": ["requestor"]},
    "user_status/.POST": {
        "function": add_status,
        "params": ["requestor", "user_id", "score"],
    },
    "user_status/$status_id.GET": {
        "function": get_status,
        "params": ["requestor", "status_id"],
    },
    "user_status/$status_id.PUT": {
        "function": update_status,
        "params": ["requestor", "status_id", "score"],
    },
    "user_status/$status_id.DELETE": {
        "function": delete_status,
        "params": ["requestor", "status_id"],
    },
    "guessinggame/$gg_id.GET": {"function": get_gg, "params": ["requestor", "game_id"]},
    "guessinggame/$gg_id.PUT": {
        "function": update_media_and_status,
        "params": ["requestor", "game_id", "media_ids", "status_ids"],
    },
    "guessinggame/$gg_id.POST": {
        "function": update_gg_end_time,
        "params": ["requestor", "game_id", "end_time"],
    },
    "guessinggame/$gg_id.DELETE": {
        "function": delete_gg,
        "params": ["requestor", "game_id"],
    },
    "guessinggame/.GET": {"function": get_all_ggs, "params": ["requestor"]},
    "guessinggame/.POST": {
        "function": add_gg,
        "params": [
            "requestor",
            "start_date",
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
        "params": ["requestor", "name", "description", "start_date", "end_date"],
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
    "media/affiliations.GET": {
        "function": get_media_by_affiliations,
        "params": ["requestor", "affiliation_ids"],
        "optional": ["limit", "count_only"],
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
            "name_id",
            "former_name_id",
            "gender",
            "description",
            "height",
            "display_id",
            "social_id",
            "location_id",
            "tag_ids",
            "blood_type",
            "call_count",
            "birth_date",
            "death_date"
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
            "description",
            "company_id",
            "display_id",
            "website",
            "social_id",
            "tag_ids",
            "debut_date",
            "disband_date"
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
        "optional": ["guild_id"],
    },
    "channel/$channel_id.DELETE": {
        "function": delete_channel,
        "params": ["requestor", "channel_id"],
    },
}
