from . import (
    self,
    check_permission,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
    is_int64,
)
from models import Requestor


@check_permission(permission_level=DEVELOPER)
async def add_channel(requestor: Requestor, channel_id: int, guild_id: int = None):
    """Add a channel."""
    is_int64(channel_id)
    if guild_id is not None:
        is_int64(guild_id)
    return await self.db.execute(
        "SELECT public.addchannel($1, $2)", channel_id, guild_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_channel(requestor: Requestor, channel_id: int):
    """Delete a channel."""
    is_int64(channel_id)
    return await self.db.execute("SELECT public.deletechannel($1})", channel_id)


@check_permission(permission_level=DEVELOPER)
async def get_channel(requestor: Requestor, channel_id: int):
    """Get a channel."""
    is_int64(channel_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.getchannels WHERE channelid = $1", channel_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_channels(requestor: Requestor):
    """Get all channels."""
    return await self.db.fetch("SELECT * FROM public.getchannels")
