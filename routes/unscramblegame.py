import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.unscramblegame as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

us = PintBlueprint("unscramblegame", __name__, url_prefix="/unscramblegame/")


@us.route("<int:us_id>")
@us.doc(
    params={
        "us_id": "UnscrambleGame ID to manage.",
    }
)
class UnscrambleGame(Resource):
    async def get(self, us_id: int):
        """Get an unscramble game.

        Use this route to get an unscramble game.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_us(requestor, us_id)

    async def delete(self, us_id: int):
        """
        Delete an unscramble game.

        Use this route to delete an unscramble game. This will cascade all objects dependent
        and is not reversible.

        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_us(requestor, us_id)

    async def put(self, us_id: int):
        """
        Update the status IDs of an unscramble game.

        Use this route to update the status IDs of an unscramble game.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.update_status(
            requestor, us_id, request.args.get("status_ids")
        )


@us.route("")
@us.doc()
class GeneralUnscrambleGame(Resource):
    async def get(self):
        """Get all Unscramble Games

        Use this route to get all guessing games.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_all_uss(requestor)

    async def post(self):
        """Add an unscramble game.

        Use this route to add an unscramble game.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_us(
            requestor,
            date_id=request.args.get("date_id"),
            status_ids=request.args.get("status_ids"),
            mode_id=request.args.get("mode_id"),
            difficulty_id=request.args.get("difficulty_id"),
        )
