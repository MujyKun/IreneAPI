import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.userstatus as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

status = PintBlueprint("status", __name__, url_prefix="/user_status/")


@status.route("<int:status_id>")
@status.doc(
    params={
        "date_id": "Status ID to manage.",
    }
)
class UserStatus(Resource):
    async def get(self, status_id: int):
        """Get a status.

        Use this route to get a status.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_status(requestor, status_id)

    async def delete(self, status_id: int):
        """Delete a status.

        Use this route to delete a status. This will cascade all objects dependent on the date and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_status(requestor, status_id)

    async def put(self, status_id: int):
        """Updates a status.

        Use this route to update a date's end date.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.update_status(
            requestor, status_id, request.args.get("score")
        )


@status.route("")
@status.doc()
class UserStatuses(Resource):
    async def get(self):
        """Get all statuses.

        Use this route to get all statuses.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_statuses(requestor)

    async def post(self):
        """Add a status.

        Use this route to add a status.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_status(
            requestor, request.args.get("user_id"), request.args.get("score")
        )
