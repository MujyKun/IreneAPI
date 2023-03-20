import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

position = PintBlueprint("position", __name__, url_prefix="/position/")


@position.route("<int:position_id>")
@position.doc(
    params={
        "position_id": "Position ID to manage.",
    }
)
class Position(Resource):
    async def get(self, position_id: int):
        """Get a position.

        Use this route to get a position.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_position(requestor, position_id)

    async def post(self, position_id: int):
        """Add a position.

        Use this route to add a position.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_position(requestor, position_id)

    async def delete(self, position_id: int):
        """Delete a position.

        Use this route to delete a position. This will cascade all objects dependent on the position and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_position(requestor, position_id)


@position.route("")
@position.doc()
class Positions(Resource):
    async def get(self):
        """Get all positions.

        Use this route to get all positions.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_positions(requestor)
