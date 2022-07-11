import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.twitch as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

twitch = PintBlueprint("twitch", __name__, url_prefix="/twitch/")


@twitch.route("<int:username>")
@twitch.doc(
    params={
        "username": "Twitch username to manage.",
    }
)
class TwitchChannel(Resource):
    async def get(self, username: str):
        """Get a Twitch Channel.

        Use this route to get a Twitch Channel.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_twitch_channel(requestor, username)

    async def delete(self, username: str):
        """Unsubscribe from a twitch channel.

        Use this route to unsubscribe from a twitch channel.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.unsubscribe_from_twitch_channel(
            requestor, username, request.args.get("channel_id")
        )

    async def post(self, username: str):
        """Subscribe to a twitch channel.

        Use this route to subscribe to a twitch channel.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.subscribe_to_twitch_channel(
            requestor,
            username=username,
            guild_id=request.args.get("guild_id"),
            channel_id=request.args.get("channel_id"),
            role_id=request.args.get("role_id"),
        )

    async def put(self, username: str):
        """Change whether a channel has been posted to.

        Use this route to change the flag whether a channel has been posted to.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.update_posted(
            requestor,
            username=username,
            channel_ids=request.args.get("channel_ids"),
            posted=request.args.get("posted"),
        )


@twitch.route("")
@twitch.doc()
class TwitchChannels(Resource):
    async def get(self):
        """Get all channels.

        Use this route to get all channels.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_twitch_channels(requestor)


@twitch.route("filter/$guild_id")
@twitch.doc(
    params={
        "guild_id": "Discord Guild ID.",
    }
)
class TwitchChannelsFilter(Resource):
    async def get(self, guild_id):
        """Get all channels affiliated with a guild.

        Use this route to get all channels affiliated with a guild.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_twitch_channels_by_guild(requestor, guild_id)


@twitch.route("is_live")
@twitch.doc()
class TwitchIsLive(Resource):
    async def get(self):
        """
        Get the live status of twitch accounts.

        Use this route to get the live status of twitch accounts.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.is_live(requestor, usernames=request.args.get("usernames"))


@twitch.route("exists/$username")
@twitch.doc(
    params={
        "username": "Twitch username to confirm if it exists.",
    }
)
class TwitchExists(Resource):
    async def get(self, username):
        """
        Check if a twitch username exists.

        Use this route to check if a username exists.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.username_exists(
            requestor, username=request.args.get("username")
        )


@twitch.route("already_posted/$username")
@twitch.doc(
    params={
        "username": "Twitch username to check if already posted to a discord channel.",
    }
)
class TwitchAlreadyPosted(Resource):
    async def get(self, username):
        """
        Get all discord channels that have posted messages.

        Use this route to check which discord channels have posted messages.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_posted(requestor, username=request.args.get("username"))
