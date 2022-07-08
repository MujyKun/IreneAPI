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
async def get_all_ggs(requestor: Requestor) -> dict:
    """Get all guessing game information."""
    return await self.db.fetch("SELECT * FROM guessinggame.getggs")


@check_permission(permission_level=DEVELOPER)
async def get_gg(requestor: Requestor, game_id: int) -> dict:
    """Get a specific guessing game's information."""
    return await self.db.fetch_row(
        "SELECT * FROM guessinggame.getggs WHERE gameid = $1", game_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_gg(requestor: Requestor, game_id: int) -> dict:
    """Get all guessing game information."""
    return await self.db.execute("SELECT guessinggame.deletegg($1)", game_id)


@check_permission(permission_level=DEVELOPER)
async def add_gg(
    requestor: Requestor,
    date_id,
    media_ids,
    status_ids,
    mode_id,
    difficulty_id,
    is_nsfw,
) -> dict:
    """Add a guessing game."""
    return await self.db.fetch_row(
        "SELECT * FROM guessinggame.addgg($1, $2, $3, $4, $5, $6)",
        date_id,
        media_ids,
        status_ids,
        mode_id,
        difficulty_id,
        is_nsfw,
    )
