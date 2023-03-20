from . import (
    self,
    check_permission,
    hash_token,
    is_int64,
    GOD,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
)
from models import Requestor


@check_permission(permission_level=DEVELOPER)
async def add_token(
    requestor: Requestor, user_id: int, unhashed_token: str, access_id: int
):
    """Add an API token for a user."""
    is_int64(user_id)
    await self.db.execute(
        "SELECT public.addtoken($1, $2, $3)",
        user_id,
        hash_token(unhashed_token),
        access_id,
    )


@check_permission(permission_level=DEVELOPER)
async def get_token(requestor: Requestor, user_id: int):
    """Get a user's hashed API token."""
    is_int64(user_id)
    return await self.db.fetch_row(f"SELECT public.gettoken($1)", user_id)


@check_permission(permission_level=USER)
async def check_token_exists(requestor: Requestor, user_id: int):
    """Check if a user's API token exists."""
    is_int64(user_id)
    return await self.db.fetch_row(f"SELECT public.gettokenexists($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_token(requestor: Requestor, user_id: int):
    """Get a user's hashed API token."""
    is_int64(user_id)
    return await self.db.fetch_row(f"SELECT public.deletetoken($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def get_permission_level(requestor: Requestor, user_id: int):
    """Get the permission level a user has access to."""
    is_int64(user_id)
    return await self.db.fetch_row(f"SELECT public.getaccessid($1)", user_id)
