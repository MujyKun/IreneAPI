import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

location = PintBlueprint("location", __name__, url_prefix="/location/")


@location.route("<int:location_id>")
@location.doc(
    params={
        "location_id": "Location ID to manage.",
    }
)
class Location(Resource):
    async def get(self, location_id: int):
        """Get a location.

        Use this route to get a location.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_location(requestor, location_id)

    async def delete(self, location_id: int):
        """Delete a location.

        Use this route to delete a location. This will cascade all objects dependent on the location and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_location(requestor, location_id)


@location.route("")
@location.doc()
class Locations(Resource):
    async def get(self):
        """Get all locations.

        Use this route to get all locations.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_locations(requestor)

    async def post(self):
        """Add a location.

        Use this route to add a location.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_location(
            requestor,
            country=request.args.get("country"),
            city=request.args.get("city"),
        )
