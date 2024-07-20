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
async def get_all_uss(requestor: Requestor) -> dict:
    """Get all unscramble game information."""
    return await self.db.fetch("SELECT * FROM unscramblegame.games")


@check_permission(permission_level=DEVELOPER)
async def update_status(requestor: Requestor, game_id, status_ids) -> dict:
    """Update status IDs for a game."""
    return await self.db.execute(
        "SELECT unscramblegame.updatestatus($1, $2)", game_id, status_ids
    )


@check_permission(permission_level=DEVELOPER)
async def get_us(requestor: Requestor, game_id: int) -> dict:
    """Get a specific unscramble game's information."""
    return await self.db.fetch_row(
        "SELECT * FROM unscramblegame.games WHERE gameid = $1", game_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_us(requestor: Requestor, game_id: int) -> dict:
    """Delete an unscramble game."""
    return await self.db.execute("SELECT unscramblegame.deleteus($1)", game_id)


@check_permission(permission_level=DEVELOPER)
async def add_us(
    requestor: Requestor, start_date, status_ids, mode_id, difficulty_id
) -> dict:
    """Add an unscramble game."""
    return await self.db.fetch_row(
        "SELECT * FROM unscramblegame.addus($1, $2, $3, $4)",
        convert_to_timestamp(start_date),
        status_ids,
        mode_id,
        difficulty_id,
    )


@check_permission(permission_level=DEVELOPER)
async def update_us_end_time(
    requestor: Requestor,
    game_id,
    end_time
) -> dict:
    """Update the end time of an unscramble game."""
    return await self.db.fetch_row(
        "UPDATE unscramblegame.games SET enddate = $1 "
        "WHERE gameid = $2",
        convert_to_timestamp(end_time), game_id)
