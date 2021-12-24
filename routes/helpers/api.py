from . import self, check_permission
from models import Requestor


@check_permission(permission_level=1)
async def add_token(
    requestor: Requestor, user_id: int, unhashed_token: str, access_id: int
):
    """Add an API token for a user."""
    await self.db.execute(
        f"SELECT public.addtoken({user_id}, '{unhashed_token}', {access_id})"
    )


@check_permission(permission_level=1)
async def get_token(requestor: Requestor, user_id: int):
    """Get a user's hashed API token."""
    token = await self.db.fetch_row(f"SELECT public.gettoken({user_id})")
    return None if not token else token[0]


@check_permission(permission_level=1)
async def get_permission_level(requestor: Requestor, user_id: int):
    """Get the permission level a user has access to."""
    permissions_level = await self.db.fetch_row(f"SELECT public.getaccess({user_id})")
    return None if not permissions_level else permissions_level[0]
