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
async def get_ban_phrase(requestor: Requestor, phrase_id: int):
    is_int64(phrase_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.getbanphrases WHERE phraseid = $1", phrase_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_ban_phrase(requestor: Requestor, phrase_id: int):
    is_int64(phrase_id)
    return await self.db.execute("SELECT public.deletebanphrase($1)", phrase_id)


@check_permission(permission_level=DEVELOPER)
async def get_ban_phrases(requestor: Requestor):
    return await self.db.fetch("SELECT * FROM public.getbanphrases")


@check_permission(permission_level=DEVELOPER)
async def add_ban_phrase(
    requestor: Requestor, guild_id: int, log_channel_id: int, phrase: str, punishment: str
):
    is_int64(guild_id)
    is_int64(log_channel_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.addbanphrase($1, $2, $3, $4)",
        guild_id,
        log_channel_id,
        phrase,
        punishment
    )
