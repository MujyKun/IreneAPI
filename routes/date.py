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

date = PintBlueprint("date", __name__, url_prefix="/date/")


@date.route("<int:date_id>")
@date.doc(
    params={
        "date_id": "Date ID to manage.",
    }
)
class Date(Resource):
    async def get(self, date_id: int):
        """Get a date.

        Use this route to get a date.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_date(requestor, date_id)

    async def delete(self, date_id: int):
        """Delete a date.

        Use this route to delete a date. This will cascade all objects dependent on the date and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_date(requestor, date_id)

    async def put(self, date_id: int):
        """Updates a date.

        Use this route to update a date's end date.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.update_date(
            requestor, date_id, request.args.get("end_date")
        )


@date.route("")
@date.doc()
class Dates(Resource):
    async def get(self):
        """Get all dates.

        Use this route to get all dates.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_dates(requestor)

    async def post(self):
        """Add a date.

        Use this route to add a date.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_date(
            requestor, request.args.get("start_date"), request.args.get("end_date")
        )
