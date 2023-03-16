import aiohttp


class Twitch:
    def __init__(self):
        from . import keys

        self.__client_secret = keys.twitch_client_secret
        self.__client_id = keys.twitch_client_id

        self.__reset_token_endpoint = f"https://id.twitch.tv/oauth2/token?client_id={self.__client_id}&client_secret={self.__client_secret}&grant_type=client_credentials"
        self.session = aiohttp.ClientSession()
        self.__twitch_token = None

    @property
    def __headers(self):
        return {
            "Authorization": f"Bearer {self.__twitch_token}",
            "client-id": self.__client_id,
        }

    async def reset_token(self):
        """Get and reset twitch token to use on the twitch api."""
        async with self.session.post(self.__reset_token_endpoint) as r:
            if r.status == 200:
                body = await r.json()
                self.__twitch_token = body.get("access_token")
                return self.__twitch_token
        self.__twitch_token = None

    async def check_live(self, twitch_username: str) -> bool:
        """
        Check if a twitch account is live.

        :param twitch_username: str
            The twitch username to check that is live.
        :returns bool:
            Whether the account is live.
        """
        if not self.__twitch_token:
            await self.reset_token()

        end_point = f"https://api.twitch.tv/helix/search/channels?query={twitch_username}&live_only=true"
        async with self.session.get(end_point, headers=self.__headers) as r:
            if r.status == 200:
                data = (await r.json())["data"]
                for streamer in data:
                    broadcaster_login = streamer["broadcaster_login"]
                    display_name = streamer["display_name"]
                    is_live = streamer.get("is_live")
                    if (
                        twitch_username.lower()
                        in [
                            broadcaster_login.lower(),
                            display_name.lower(),
                        ]
                        and is_live
                    ):
                        return True
            elif r.status == 401:
                await self.reset_token()
                return await self.check_live(twitch_username)  # recursive
        return False

    async def check_exists(self, twitch_username) -> bool:
        """
        Check if a username exists.

        :param twitch_username: str
            The twitch username to check exists.
        :returns: bool
            Whether the twitch account exists.
        """
        if not self.__twitch_token:
            await self.reset_token()

        end_point = (
            f"https://api.twitch.tv/helix/search/channels?query={twitch_username}"
        )
        async with self.session.get(end_point, headers=self.__headers) as r:
            if r.status == 200:
                data = (await r.json())["data"]
                for streamer in data:
                    broadcaster_login = streamer["broadcaster_login"]
                    display_name = streamer["display_name"]
                    if twitch_username.lower() in [
                        broadcaster_login.lower(),
                        display_name.lower(),
                    ]:
                        return True
            elif r.status == 401:
                await self.reset_token()
                return await self.check_exists(twitch_username)
        return False
