import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.twitter as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

twitter = PintBlueprint("twitter", __name__, url_prefix="/twitter/")


@twitter.route("<int:twitter_id>")
@twitter.doc(params={"twitter_id": "Twitter Account ID to manage."})
class TwitterAccount(Resource):
    async def get(self, twitter_id):
        """Get the timeline of a Twitter account.

        Use this route to get the timeline of a Twitter account.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_timeline(requestor, twitter_id)


@twitter.route("account/$username")
@twitter.doc(params={"username": "Twitter Username to manage."})
class TwitterUsername(Resource):
    async def post(self, username):
        """
        Get (and Add) a Twitter Account.

        Use this route to get a Twitter account's ID and insert it
        into the database (if it does not already exist).
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_and_add_twitter_id(requestor, username)


@twitter.route("")
@twitter.doc()
class TwitterAllSubscriptions(Resource):
    async def get(self):
        """Get all Twitter subscriptions.

        Use this route to get all Twitter subscriptions.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_all_subscriptions(requestor)


@twitter.route("<string:username>")
@twitter.doc(params={"username": "Twitter Account Username to manage."})
class TwitterSubscriptions(Resource):
    async def get(self, username):
        """Get the subscriptions for a specific Twitter username.

        Use this route to get the subscriptions for a specific Twitter account.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_subscriptions(requestor, username=username)


@twitter.route("modify/$twitter_id")
@twitter.doc(params={"twitter_id": "Twitter Account ID to manage."})
class TwitterSubscriptionsModify(Resource):
    async def delete(self, twitter_id):
        """Unsubscribe from a Twitter account.

        Use this route to unsubscribe from a Twitter account.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_twitter_subscription(
            requestor, twitter_id=twitter_id, channel_id=request.args.get("channel_id")
        )

    async def post(self, twitter_id):
        """Subscribe to a Twitter account.

        Use this route to subscribe to a Twitter account.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_twitter_subscription(
            requestor,
            twitter_id=twitter_id,
            channel_id=request.args.get("channel_id"),
            role_id=request.args.get("role_id"),
        )


@twitter.route("exists/$username")
@twitter.doc(
    params={
        "username": "Twitter username to confirm if it exists.",
    }
)
class TwitterExists(Resource):
    async def get(self, username):
        """Check if a Twitter username exists.

        Use this route to check if a Twitter username exists.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.username_exists(
            requestor, username=request.args.get("username")
        )


@twitter.route("filter/$guild_id")
@twitter.doc(
    params={
        "guild_id": "Discord Guild ID.",
    }
)
class TwitterFilter(Resource):
    async def get(self, guild_id):
        """Get all channels affiliated with a guild.

        Use this route to get all channels affiliated with a guild.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_twitter_channels_by_guild(requestor, guild_id)
