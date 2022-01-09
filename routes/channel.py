import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.channel as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

channel = PintBlueprint("channel", __name__, url_prefix="/channel/")


@channel.route("<int:channel_id>")
@channel.doc(
    params={
        "channel_id": "Channel ID to manage.",
    }
)
class Channel(Resource):
    async def post(self, channel_id: int):
        """Add a channel.

        Use this route to add a channel.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_channel(requestor, channel_id)

    async def delete(self, channel_id: int):
        """Delete a channel.

        Use this route to delete a channel. This will cascade all objects dependent on the channel and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_channel(requestor, channel_id)
