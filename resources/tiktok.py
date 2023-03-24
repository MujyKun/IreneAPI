

class Tiktok:
    def __init__(self):
        ...

    async def get_recent_video_id(self, tiktok_username: str):
        """
        Check if a twitch account is live.

        :param twitch_username: str
            The twitch username to check that is live.
        :returns bool:
            Whether the account is live.
        """
        tiktok_username = tiktok_username.replace("@", "")
