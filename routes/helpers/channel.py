from . import self, check_permission
from models import Requestor


@check_permission(permission_level=1)
async def add_channel(requestor: Requestor, channel_id: int):
    """Add a channel."""
    await self.db.execute(f"SELECT public.addchannel({channel_id})")


@check_permission(permission_level=1)
async def delete_channel(requestor: Requestor, channel_id: int):
    """Delete a channel."""
    await self.db.execute(f"SELECT public.deletechannel({channel_id})")

