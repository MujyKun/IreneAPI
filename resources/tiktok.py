from tiktokapipy.async_api import AsyncTikTokAPI


class Tiktok:
    @staticmethod
    async def get_recent_video_id(tiktok_username: str) -> dict:
        """
        Get the most recent TikTok video of a user.

        :param tiktok_username: str
            The TikTok username to check videos for.
        :returns: int
            Latest video ID.
        """
        tiktok_username = tiktok_username.replace("@", "")
        async with AsyncTikTokAPI() as api:
            user = await api.user(tiktok_username)
            async for video in user.videos:
                return {tiktok_username: video.id}
