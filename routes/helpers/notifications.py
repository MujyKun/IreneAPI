from typing import List

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
async def get_noti(requestor: Requestor, noti_id: int):
    is_int64(noti_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.notifications WHERE notiid = $1", noti_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_noti(requestor: Requestor, noti_id: int):
    is_int64(noti_id)
    return await self.db.execute("SELECT public.deletenotification($1)", noti_id)


@check_permission(permission_level=DEVELOPER)
async def get_notifications(requestor: Requestor):
    return await self.db.fetch("SELECT * FROM public.notifications")


@check_permission(permission_level=DEVELOPER)
async def add_notification(
    requestor: Requestor, guild_id: int, user_id: int, phrase: str
):
    is_int64(guild_id)
    is_int64(user_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.addnotification($1, $2, $3)",
        guild_id,
        user_id,
        phrase,
    )
