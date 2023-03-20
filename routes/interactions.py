import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.interactions as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

interactions = PintBlueprint("interactions", __name__, url_prefix="/interactions/")


@interactions.route("")
@interactions.doc()
class Interactions(Resource):
    async def get(self):
        """Get all interactions.

        Use this route to get all interactions.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_interactions(requestor)

    async def post(self):
        """Add an interaction.

        Use this route to add an interaction
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_interaction(
            requestor, request.args.get("type_id"), request.args.get("url")
        )

    async def delete(self):
        """Delete an interaction.

        Use this route to delete an interaction
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_interaction(
            requestor, request.args.get("type_id"), request.args.get("url")
        )


@interactions.route("type/")
@interactions.doc()
class InteractionTypes(Resource):
    async def post(self):
        """Add an interaction type.

        Use this route to add an interaction type
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_interaction_type(requestor, request.args.get("name"))

    async def delete(self):
        """Delete an interaction type.

        Use this route to delete an interaction type
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_interaction_type(
            requestor, request.args.get("type_id")
        )
