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


@check_permission(permission_level=DEVELOPER)
async def update_status(requestor: Requestor, status_id: int, score: int) -> dict:
    """Update the score."""
    return await self.db.fetch_row(
        "SELECT * FROM updateuserstatus($1, $2)", status_id, score
    )


@check_permission(permission_level=DEVELOPER)
async def delete_status(requestor: Requestor, status_id) -> dict:
    """Delete status information."""
    return await self.db.execute("SELECT * FROM deleteuserstatus($1)", status_id)


@check_permission(permission_level=USER)
async def get_status(requestor: Requestor, status_id: int) -> dict:
    """Get a status's information."""
    is_int64(status_id)
    return await self.db.fetch_row(
        "SELECT * FROM getuserstatuses WHERE statusid = $1", status_id
    )


@check_permission(permission_level=USER)
async def get_statuses(requestor: Requestor) -> dict:
    """Get all status information."""
    return await self.db.fetch("SELECT * FROM getuserstatuses")


@check_permission(permission_level=DEVELOPER)
async def add_status(requestor: Requestor, user_id: int, score: int) -> dict:
    """Add a status."""
    return await self.db.fetch_row(
        "SELECT * FROM adduserstatus($1, $2)", user_id, score
    )
