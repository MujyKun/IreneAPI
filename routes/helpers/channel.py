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
