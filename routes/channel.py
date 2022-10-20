import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

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
    async def get(self, channel_id: int):
        """Get a channel.

        Use this route to get a channel.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_channel(requestor, channel_id)

    async def delete(self, channel_id: int):
        """Delete a channel.

        Use this route to delete a channel. This will cascade all objects dependent on the channel and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_channel(requestor, channel_id)


@channel.route("")
@channel.doc()
class Channels(Resource):
    async def get(self):
        """Get all channels.

        Use this route to get all channels.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_channels(requestor)

    async def post(self):
        """Add a channel.

        Use this route to add a channel.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_channel(
            requestor,
            channel_id=request.args.get("channel_id"),
            guild_id=request.args.get("guild_id"),
        )
