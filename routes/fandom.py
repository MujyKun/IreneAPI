import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

fandom = PintBlueprint("fandom", __name__, url_prefix="/fandom/")


@fandom.route("<int:group_id>")
@fandom.doc(
    params={
        "group_id": "Group ID to manage.",
    }
)
class Fandom(Resource):
    async def get(self, group_id: int):
        """Get fandoms belonging to a group.

        Use this route to get a group's fandoms.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_fandoms_by_group(requestor, group_id)

    async def post(self, group_id: int):
        """Add a fandom to a group.

        Use this route to add a fandom to a group.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_fandom(
            requestor, group_id, request.args.get("fandom_name")
        )

    async def delete(self, group_id: int):
        """Delete a fandom belonging to a group.

        Use this route to delete a fandom. Not Reversible.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_fandom(
            requestor, group_id, request.args.get("fandom_name")
        )


@fandom.route("")
@fandom.doc()
class Fandoms(Resource):
    async def get(self):
        """Get all fandoms.

        Use this route to get all fandoms.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_fandoms(requestor)
