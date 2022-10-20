import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.guessinggame as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

gg = PintBlueprint("guessinggame", __name__, url_prefix="/guessinggame/")


@gg.route("<int:gg_id>")
@gg.doc(
    params={
        "gg_id": "GuessingGame ID to manage.",
    }
)
class GuessingGame(Resource):
    async def get(self, gg_id: int):
        """Get a guessing game.

        Use this route to get a guessing game.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_gg(requestor, gg_id)

    async def delete(self, gg_id: int):
        """
        Delete a guessing game.

        Use this route to delete a guessing game. This will cascade all objects dependent
        and is not reversible.

        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_gg(requestor, gg_id)

    async def put(self, gg_id: int):
        """
        Update a guessing game's media and status ids.

        Use this route to update a guessing game's media & status ids.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.update_media_and_status(
            requestor,
            gg_id,
            request.args.get("media_ids"),
            request.args.get("status_ids"),
        )


@gg.route("")
@gg.doc()
class GeneralGuessingGame(Resource):
    async def get(self):
        """Get all Guessing Games

        Use this route to get all guessing games.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_all_ggs(requestor)

    async def post(self):
        """Add a guessing game.

        Use this route to add a guessing game.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_gg(
            requestor,
            date_id=request.args.get("date_id"),
            media_ids=request.args.get("media_ids"),
            status_ids=request.args.get("status_ids"),
            mode_id=request.args.get("mode_id"),
            difficulty_id=request.args.get("difficulty_id"),
            is_nsfw=request.args.get("is_nsfw"),
        )
