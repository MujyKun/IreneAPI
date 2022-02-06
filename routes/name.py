import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

name = PintBlueprint("name", __name__, url_prefix="/name/")


@name.route("<int:name_id>")
@name.doc(
    params={
        "name_id": "Name ID to manage.",
    }
)
class Name(Resource):
    async def get(self, name_id: int):
        """Get a name.

        Use this route to get a name.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_name(requestor, name_id)

    async def delete(self, name_id: int):
        """Delete a name.

        Use this route to delete a name. This will cascade all objects dependent on the name and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_name(requestor, name_id)


@name.route("")
@name.doc()
class Names(Resource):
    async def get(self):
        """Get all names.

        Use this route to get all names.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_names(requestor)

    async def post(self):
        """Add a name.

        Use this route to add a name.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_name(
            requestor, request.args.get("first_name"), request.args.get("last_name")
        )
