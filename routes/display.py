import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

display = PintBlueprint("display", __name__, url_prefix="/display/")


@display.route("<int:display_id>")
@display.doc(
    params={
        "display_id": "Display ID to manage.",
    }
)
class Display(Resource):
    async def get(self, display_id: int):
        """Get a display.

        Use this route to get a display.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_display(requestor, display_id)

    async def delete(self, display_id: int):
        """Delete a display.

        Use this route to delete a display. This will cascade all objects dependent on the display and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_display(requestor, display_id)


@display.route("")
@display.doc()
class Displays(Resource):
    async def get(self):
        """Get all displays.

        Use this route to get all displays.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_displays(requestor)

    async def post(self):
        """Add a display.

        Use this route to add a display.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_display(
            requestor,
            avatar=request.args.get("avatar"),
            banner=request.args.get("banner"),
        )
