from . import self, check_permission, OWNER, DEVELOPER, SUPER_PATRON, FRIEND, USER
from models import Requestor


@check_permission(permission_level=DEVELOPER)
async def add_channel(requestor: Requestor, channel_id: int):
    """Add a channel."""
    return await self.db.execute("SELECT public.addchannel($1)", channel_id)


@check_permission(permission_level=DEVELOPER)
async def delete_channel(requestor: Requestor, channel_id: int):
    """Delete a channel."""
    return await self.db.execute("SELECT public.deletechannel($1})", channel_id)


@check_permission(permission_level=DEVELOPER)
async def get_channel(requestor: Requestor, channel_id: int):
    """Get a channel."""
    return await self.db.fetch_row(
        "SELECT * FROM public.getchannels WHERE channelid = $1", channel_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_channels(requestor: Requestor):
    """Get all channels."""
    return await self.db.fetch("SELECT * FROM public.getchannels")
