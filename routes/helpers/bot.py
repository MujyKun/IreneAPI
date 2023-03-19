from . import (
    self,
    check_permission,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
    is_int64,
    COMMANDS_FILE_NAME,
)
from models import Requestor
import aiofiles
import json


@check_permission(permission_level=DEVELOPER)
async def update_commands(requestor: Requestor, commands):
    """Update commands."""
    async with aiofiles.open(COMMANDS_FILE_NAME, "w") as file:
        json_data = json.dumps(commands)
        await file.write(json_data)


@check_permission(permission_level=USER)
async def get_commands(requestor: Requestor):
    """Get all commands."""
    async with aiofiles.open(COMMANDS_FILE_NAME, "r") as file:
        json_data = await file.read()
        data = json.loads(json_data)
        return data
