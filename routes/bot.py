import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.bot as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

bot = PintBlueprint("bot", __name__, url_prefix="/bot/")


@bot.route("commands")
@bot.doc()
class Commands(Resource):
    async def put(self):
        """Update commands.

        Use this route to update the list of commands.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.update_commands(requestor, request.args.get("commands"))

    async def get(self):
        """
        Get all commands

        Use this route to get all commands.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_commands(requestor)
