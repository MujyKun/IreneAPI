import datetime
from typing import Optional

import peony.exceptions
from peony.oauth_dance import oauth_dance, get_access_token
from peony import PeonyClient
from . import keys


class Twitter(PeonyClient):
    """
    Twitter API v2.0 usage.
    """

    def __init__(
        self,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        api_version="2",
        suffix="",
    ):
        super(Twitter, self).__init__(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            api_version=api_version,
            suffix=suffix,
        )
        self.usage_cap_exceeded_title = "UsageCapExceeded"
        self.exceeded = False
        self.last_tried_at = datetime.datetime.now()

    async def set_exceeded(self, flag=True):
        """Manage an exceeded limit of api requests."""
        self.last_tried_at = datetime.datetime.now()
        self.exceeded = flag

    async def get_user_timeline(self, user_id: str = None, username: str = None):
        """
        Get a user's timeline.

        Always pass in a user id if it is available. Inputting a username will use another request.

        :param user_id: (str) The user's twitter id to look up their timeline.
        :param username: (str) The user's username to look up their timeline.

        """
        if not user_id and not username:
            return

        if user_id:
            user_id = str(user_id)

        try:
            info = await self.api.users[
                user_id if user_id else (await self.get_user_id(username))
            ].tweets.get()
            await self.set_exceeded(flag=False)
            return info
        except peony.exceptions.HTTPTooManyRequests as e:
            await self.set_exceeded(flag=True)

        return {}

    async def get_user_id(self, username) -> Optional[int]:
        """
        Get a Twitter user's id based on their username.

        :param username: (str) The user's username.
        """
        try:
            response = await self.api.users.by.username[username].get()
            await self.set_exceeded(flag=False)
            if response.get("data"):
                return int(response["data"]["id"])
        # any other exceptions should be raised.
        except peony.exceptions.HTTPBadRequest as e:
            return None
        except peony.exceptions.HTTPTooManyRequests as e:
            await self.set_exceeded(flag=True)

    async def me(self):
        """
        Return information about the connected client.
        """
        return await self.api.users.me.get()
