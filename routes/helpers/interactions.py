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
async def get_interactions(requestor: Requestor):
    """Get all interactions."""
    return await self.db.fetch("SELECT * FROM interactions.getinteractions")


@check_permission(permission_level=DEVELOPER)
async def add_interaction(requestor: Requestor, type_id, url):
    """Add an interaction."""
    is_int64(type_id)
    return await self.db.fetch_row(
        "SELECT * FROM interactions.addinteraction($1, $2)", type_id, url
    )


@check_permission(permission_level=DEVELOPER)
async def delete_interaction(requestor: Requestor, type_id: int, url):
    """Delete an interaction."""
    is_int64(type_id)
    return await self.db.fetch(
        "SELECT * FROM interactions.deleteinteraction($1, $2)", type_id, url
    )


@check_permission(permission_level=DEVELOPER)
async def add_interaction_type(requestor: Requestor, name):
    """Add an interaction type."""
    return await self.db.fetch(
        "SELECT * FROM interactions.addinteractiontype($1)", name
    )


@check_permission(permission_level=DEVELOPER)
async def delete_interaction_type(requestor: Requestor, type_id: int):
    """Delete an interaction type."""
    is_int64(type_id)
    return await self.db.fetch(
        "SELECT * FROM interactions.deleteinteractiontype($1)", type_id
    )
