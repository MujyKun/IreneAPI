from . import self, check_permission
from models import Requestor
from . import hash_token


@check_permission(permission_level=1)
async def add_token(
    requestor: Requestor, user_id: int, unhashed_token: str, access_id: int
):
    """Add an API token for a user."""

    await self.db.execute(
        "SELECT public.addtoken($1, '{$2}', $3)",
        user_id,
        hash_token(unhashed_token),
        access_id,
    )


@check_permission(permission_level=1)
async def get_token(requestor: Requestor, user_id: int):
    """Get a user's hashed API token."""
    return await self.db.fetch_row(f"SELECT public.gettoken($1)", user_id)


@check_permission(permission_level=1)
async def delete_token(requestor: Requestor, user_id: int):
    """Get a user's hashed API token."""
    return await self.db.fetch_row(f"SELECT public.deletetoken($1)", user_id)


@check_permission(permission_level=1)
async def get_permission_level(requestor: Requestor, user_id: int):
    """Get the permission level a user has access to."""
    return await self.db.fetch_row(f"SELECT public.getaccessid($1)", user_id)
