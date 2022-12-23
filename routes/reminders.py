import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.reminders as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

reminders = PintBlueprint("reminders", __name__, url_prefix="/reminder/")


@reminders.route("<int:remind_id>")
@reminders.doc(params={"remind_id": "Reminder ID to manage."})
class ReminderID(Resource):
    async def delete(self, remind_id):
        """Delete a reminder.

        Use this route to delete a reminder.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_reminder(requestor, remind_id)


@reminders.route("")
@reminders.doc()
class Reminders(Resource):
    async def get(self):
        """Get all reminders.

        Use this route to get all reminders.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_reminders(requestor)

    async def post(self):
        """
        Add a reminder.

        Use this route to add a reminder.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_reminder(requestor,
                                         request.args.get("user_id"),
                                         request.args.get("reason"),
                                         request.args.get("date_id"))
