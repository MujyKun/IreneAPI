import asyncio

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
    thread_pool,
)
from models import Requestor
from resources import datadog
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


@check_permission(permission_level=DEVELOPER)
async def update_stats(requestor: Requestor, key, value):
    """Update stats to Datadog and the database."""
    is_int64(value)

    # to db
    await self.db.execute("SELECT public.addstats($1, $2)", key, value)
    # to datadog
    # datadog.send_metric(key, value)
    thread_pool.submit(datadog.send_metric, key, value)
