from typing import Optional

from peony.oauth_dance import oauth_dance, get_access_token
from peony import PeonyClient
from . import keys


class Twitter(PeonyClient):
    """
    Twitter API v2.0 usage.
    """

    def __init__(self):
        super(Twitter, self).__init__(
            consumer_key=keys.twitter_consumer_key,
            consumer_secret=keys.twitter_consumer_secret,
            access_token=keys.twitter_access_key,
            access_token_secret=keys.twitter_access_secret,
            api_version="2",
            suffix="",
        )

    async def get_user_timeline(self, user_id: str = None, username: str = None):
        """
        Get a user's timeline.

        Always pass in a user id if it is available. Inputting a username will use another request.

        :param user_id: (str) The user's twitter id to look up their timeline.
        :param username: (str) The user's username to look up their timeline.

        """
        if not user_id and not username:
            return

        return await self.api.users[
            user_id if user_id else (await self.get_user_id(username))
        ].tweets.get()

    async def get_user_id(self, username) -> Optional[int]:
        """
        Get a Twitter user's id based on their username.

        :param username: (str) The user's username.
        """
        response = await self.api.users.by.username[username].get()
        if response.get("data"):
            return int(response["data"]["id"])

    async def me(self):
        """
        Return information about the connected client.
        """
        return await self.api.users.me.get()
