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

from resources import tiktok as tiktok_obj


@check_permission(permission_level=DEVELOPER)
async def get_tiktok_accounts(requestor: Requestor) -> dict:
    """Get all TikTok accounts."""
    return await self.db.fetch("SELECT * FROM public.gettiktokchannels")


@check_permission(permission_level=DEVELOPER)
async def get_tiktok_account(requestor: Requestor, username) -> dict:
    """Get a TikTok account."""
    return await self.db.fetch_row("SELECT * FROM public.gettiktokchannels WHERE username = $1", username)


@check_permission(permission_level=DEVELOPER)
async def add_tiktok_account(
    requestor: Requestor, username: str, user_id: int, channel_id: int, role_id=None
) -> dict:
    """Add a TikTok account to the database."""
    is_int64(user_id)
    is_int64(channel_id)
    if role_id:
        is_int64(role_id)

    return await self.db.fetch(
        "SELECT public.addtiktok($1, $2, $3, $4)",
        username,
        user_id,
        channel_id,
        role_id,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_tiktok_account(
    requestor: Requestor, username: str, channel_id: int) -> dict:
    """Add a TikTok account to the database."""
    is_int64(channel_id)

    return await self.db.fetch(
        "SELECT public.deletetiktok($1, $2)", username, channel_id)


@check_permission(permission_level=DEVELOPER)
async def get_latest_tiktok_video(requestor: Requestor, username) -> dict:
    """Get the latest tiktok video for a user."""
    return await tiktok_obj.get_recent_video_id(username)
