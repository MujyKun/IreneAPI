import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.notifications as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

noti = PintBlueprint("notifications", __name__, url_prefix="/noti/")


@noti.route("<int:noti_id>")
@noti.doc(
    params={
        "noti_id": "Noti ID to manage.",
    }
)
class Noti(Resource):
    async def get(self, noti_id: int):
        """Get a noti.

        Use this route to get a noti.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_noti(requestor, noti_id)

    async def delete(self, display_id: int):
        """Delete a noti.

        Use this route to delete a noti. This will cascade all objects dependent on the display and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_noti(requestor, noti_id)


@noti.route("")
@noti.doc()
class Notifications(Resource):
    async def get(self):
        """Get all notifications.

        Use this route to get all notifications.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_notifications(requestor)

    async def post(self):
        """Add a noti.

        Use this route to add a notification.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_notification(
            requestor,
            guild_id=request.args.get("guild_id"),
            user_id=request.args.get("user_id"),
            phrase=request.args.get("phrase"),
        )
