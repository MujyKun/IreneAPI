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


@twitter.route("<int:twitter_id>/<int:channel_id>")
@twitter.doc(
    params={
        "twitter_id": "Twitter Account ID to manage the status of.",
        "channel_id": "Channel ID to associate with the Twitter account.",
    }
)
class TwitterSubscription(Resource):
    async def get(self, twitter_id: int, channel_id: int):
        """Check if a channel is subscribed to a Twitter channel.

        Use this route to check if a channel is following a Twitter account. A login is NOT needed.
        """
        requestor = Requestor(0, GOD)
        return await helper.is_subscribed(requestor, twitter_id, channel_id)

    async def post(self, twitter_id: int, channel_id: int):
        """Make a channel subscribe to a Twitter account.

        Use this route to have a channel subscribe to a Twitter account.
        Pass in a role_id as a query parameter if there is one.
        """
        requestor = await login(headers=request.headers, data=request.args)
        # TODO: If the role_id is passed in as a query parameter,
        #  then it should not interfere with the login arguments.
        return await helper.add_twitter_subscription(
            requestor, twitter_id, channel_id, *request.args
        )

    async def delete(self, twitter_id: int, channel_id: int):
        """Make a channel unsubscribe from a Twitter account.

        Use this route to have a channel unsubscribe from a Twitter account.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_twitter_subscription(
            requestor, twitter_id, channel_id
        )


@twitter.route("<str:twitter_info>/")
@twitter.doc(params={"twitter_info": "Twitter username or ID to manage the status of."})
class TwitterAccount(Resource):
    async def get(self, twitter_info: Union[int, str]):
        """Get the channels subscribed to the Twitter account.

        Use this route to get the channel ids subscribed to the Twitter account. A login is needed.
        Can pass in either a Twitter username or an Account ID.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_subscriptions(requestor, twitter_info)

    async def post(self, twitter_name: str):
        """Add a Twitter account to the Database.

        Use this route to add a Twitter account to the Database.
        It is important to note a Twitter username must be entered and not a Twitter Account ID.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_and_add_twitter_id(requestor, twitter_name)

    async def delete(self, twitter_id: int):
        """Delete a Twitter account from the Database.

        Use this route to remove a Twitter account from the Database.
        This will also drop all subscriptions to the account. Use with caution.
        It is important to note a Twitter Account ID must be entered and not a Twitter username.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_twitter_account(requestor, twitter_id)


@twitter.route("subscriptions/")
@twitter.doc()
class TwitterSubscriptions(Resource):
    async def get(self):
        """Get the channels subscribed to all Twitter accounts.

        Use this route to get the channel ids subscribed to all Twitter accounts. A login is needed.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_subscriptions(requestor=requestor)


@twitter.route("accounts/")
@twitter.doc()
class TwitterAccountInfo(Resource):
    async def get(self):
        """Get the accounts registered within the database.

        Use this route to get the account ids and Twitter usernames registered. A login is needed.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_accounts(requestor=requestor)


@twitter.route("timeline/<int:twitter_id>/")
@twitter.doc(params={"twitter_id": "Twitter Account ID to manage the status of."})
class TwitterTimeline(Resource):
    async def get(self, twitter_id: int):
        """Get the timeline of a Twitter Account.

        Use this route to get the timeline of a Twitter account. A login is needed.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_timeline(requestor=requestor, twitter_id=twitter_id)
