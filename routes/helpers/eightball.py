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


@check_permission(permission_level=USER)
async def get_response(requestor: Requestor, response_id: int) -> dict:
    """Get response information."""
    is_int64(response_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.getresponses WHERE responseid = $1",
        response_id,
    )


@check_permission(permission_level=DEVELOPER)
async def add_response(requestor: Requestor, response) -> dict:
    """Add a response"""
    return await self.db.fetch_row("SELECT * FROM public.addresponse($1)", response)


@check_permission(permission_level=DEVELOPER)
async def delete_response(requestor: Requestor, response_id) -> dict:
    """Delete an affiliation"""
    return await self.db.execute("SELECT * FROM public.deleteresponse($1)", response_id)


@check_permission(permission_level=USER)
async def get_responses(requestor: Requestor) -> dict:
    """Get all response information."""
    return await self.db.fetch("SELECT * FROM public.getresponses")
