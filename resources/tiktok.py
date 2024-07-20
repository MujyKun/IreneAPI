from typing import Dict

import aiohttp
from tiktokapipy.async_api import AsyncTikTokAPI
from tiktokapipy.models.user import user_link


class Tiktok:
    def __init__(self):
        self.user_exists: Dict[str, bool] = {}

    async def get_recent_video_id(self, tiktok_username: str) -> dict:
        """
        Get the most recent TikTok video of a user.

        :param tiktok_username: str
            The TikTok username to check videos for.
        :returns: int
            Latest video ID.
        """
        tiktok_username = tiktok_username.lower().replace("@", "")
        try:
            async with AsyncTikTokAPI() as api:
                if not await self.get_user_exists(tiktok_username):
                    raise UserWarning
                user = await api.user(tiktok_username)
                try:
                    async for video in user.videos:
                        return {tiktok_username: video.id}
                except StopAsyncIteration:  # no videos.
                    return {tiktok_username: None}
        except Exception as e:
            print(f"TikTok Search Failed -> {e}")
        return {tiktok_username: None}

    async def get_user_exists(self, tiktok_username: str) -> bool:
        """
        Get if a user exists.

        :param tiktok_username: str
            The TikTok username to check exists
        :returns: bool
            Whether the username exists.
        """
        link = user_link(tiktok_username)
        if tiktok_username not in self.user_exists:
            async with aiohttp.ClientSession().get(url=link) as r:
                self.user_exists[tiktok_username] = r.status == 200
        return self.user_exists[tiktok_username]
