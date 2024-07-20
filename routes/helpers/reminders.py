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
    convert_to_timestamp
)
from models import Requestor
from datetime import datetime


@check_permission(permission_level=DEVELOPER)
async def add_reminder(
    requestor: Requestor, user_id: int, reason: str, notify_date: str
) -> dict:
    """Add a reminder."""
    is_int64(user_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.addreminder($1, $2, $3)", user_id, reason, convert_to_timestamp(notify_date)
    )


@check_permission(permission_level=DEVELOPER)
async def delete_reminder(requestor: Requestor, remind_id: int) -> dict:
    """Delete a blood type."""
    is_int64(remind_id)
    return await self.db.execute("SELECT * FROM public.deletereminder($1)", remind_id)


@check_permission(permission_level=USER)
async def get_reminders(requestor: Requestor) -> dict:
    """Get all reminders."""
    return await self.db.fetch("SELECT * FROM public.reminders")
