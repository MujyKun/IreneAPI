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


@check_permission(permission_level=DEVELOPER)
async def get_all_ggs(requestor: Requestor) -> dict:
    """Get all guessing game information."""
    return await self.db.fetch("SELECT * FROM guessinggame.games")


@check_permission(permission_level=DEVELOPER)
async def update_media_and_status(
    requestor: Requestor, game_id, media_ids, status_ids
) -> dict:
    """Update media and status IDs for a game."""
    return await self.db.execute(
        "SELECT guessinggame.updatemediaandstatus($1, $2, $3)",
        game_id,
        media_ids,
        status_ids,
    )


@check_permission(permission_level=DEVELOPER)
async def get_gg(requestor: Requestor, game_id: int) -> dict:
    """Get a specific guessing game's information."""
    return await self.db.fetch_row(
        "SELECT * FROM guessinggame.games WHERE gameid = $1", game_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_gg(requestor: Requestor, game_id: int) -> dict:
    """Delete a guessing game."""
    return await self.db.execute("SELECT guessinggame.deletegg($1)", game_id)


@check_permission(permission_level=DEVELOPER)
async def add_gg(
    requestor: Requestor,
    start_date,
    media_ids,
    status_ids,
    mode_id,
    difficulty_id,
    is_nsfw,
) -> dict:
    """Add a guessing game."""
    return await self.db.fetch_row(
        "SELECT * FROM guessinggame.addgg($1, $2, $3, $4, $5, $6)",
        convert_to_timestamp(start_date),
        media_ids,
        status_ids,
        mode_id,
        difficulty_id,
        is_nsfw,
    )


@check_permission(permission_level=DEVELOPER)
async def update_gg_end_time(
    requestor: Requestor,
    game_id,
    end_time
) -> dict:
    """Update the end time of a guessing game."""
    return await self.db.fetch_row(
        "UPDATE guessinggame.games SET enddate = $1 "
        "WHERE gameid = $2",
        convert_to_timestamp(end_time), game_id)
