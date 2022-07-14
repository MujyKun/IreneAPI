from typing import List

from . import (
    self,
    check_permission,
    is_int64,
    GOD,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
)
from models import Requestor

from resources import twitch as twitch_obj


@check_permission(permission_level=DEVELOPER)
async def get_twitch_channels(requestor: Requestor) -> dict:
    """Get all twitch channels."""
    return await self.db.fetch("SELECT * FROM public.gettwitchchannels")


@check_permission(permission_level=DEVELOPER)
async def get_twitch_channel(requestor: Requestor, username: str) -> dict:
    """Get a specific twitch channel's information.

    NOTE: This will return several rows (each row containing a subscription)
    """
    return await self.db.fetch(
        "SELECT * FROM public.gettwitchchannels WHERE username = $1", username
    )


@check_permission(permission_level=DEVELOPER)
async def get_twitch_channels_by_guild(requestor: Requestor, guild_id: int) -> dict:
    """Get specific twitch channels subscribed to by a guild.

    NOTE: This will return several rows (each row containing a subscription)
    """
    is_int64(guild_id)
    return await self.db.fetch(
        "SELECT * FROM public.gettwitchchannels WHERE guildid = $1", guild_id
    )


@check_permission(permission_level=DEVELOPER)
async def update_posted(requestor: Requestor, username, channel_ids, posted) -> dict:
    """Change the channels posted to."""
    for channel_id in channel_ids:
        is_int64(channel_id)
    return await self.db.execute(
        "SELECT public.updateposted($1, $2, $3)", username, channel_ids, posted
    )


@check_permission(permission_level=DEVELOPER)
async def unsubscribe_from_twitch_channel(
    requestor: Requestor, username: str, channel_id: int
) -> dict:
    """Unsubscribe from a twitch channel."""
    is_int64(channel_id)
    return await self.db.execute(
        "SELECT public.unsubscribefromtwitch($1, $2)", username, channel_id
    )


@check_permission(permission_level=DEVELOPER)
async def subscribe_to_twitch_channel(
    requestor: Requestor, username, guild_id, channel_id, role_id=None
) -> dict:
    """Subscribe to a twitch channel."""
    is_int64(guild_id)
    is_int64(channel_id)
    if role_id:
        is_int64(role_id)
    return await self.db.execute(
        "SELECT * FROM public.subscribetotwitch($1, $2, $3, $4)",
        username,
        guild_id,
        channel_id,
        role_id,
    )


@check_permission(permission_level=DEVELOPER)
async def is_live(requestor: Requestor, usernames: List[str]) -> dict:
    """Check if a twitch account is live."""
    live_dict = {}
    for user in usernames:
        live_dict[user] = await twitch_obj.check_live(user)
    return {"results": live_dict}


@check_permission(permission_level=DEVELOPER)
async def username_exists(requestor: Requestor, username: str) -> dict:
    """Check if a twitch username exists."""
    exists = await twitch_obj.check_exists(username)
    return {"results": exists}


@check_permission(permission_level=DEVELOPER)
async def get_posted(requestor: Requestor, username: str) -> dict:
    """Get all discord channels that have posted messages for a specific twitch account."""
    return await self.db.fetch(
        "SELECT * FROM public.gettwitchchannels WHERE username = $1 AND posted IS TRUE",
        username,
    )
