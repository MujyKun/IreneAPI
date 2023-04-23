import datetime
from typing import Optional
import aiohttp
from .keys import theysaidso_api_key


class TheySaidSo:
    # https://theysaidso.com/api
    def __init__(self):
        self._quote_of_day: Optional[str] = None
        self._author_of_day: Optional[str] = None
        self._last_requested = None
        self._headers = headers = {
            "Accept": "application/json",
            "X-TheySaidSo-Api-Secret": theysaidso_api_key
        }
        self.api_url = "https://quotes.rest/qod?category=inspire"

    async def get_quote_of_day(self):
        """Get the quote of the day."""
        if not self._last_requested or \
                datetime.datetime.utcnow() - self._last_requested > datetime.timedelta(hours=24):
            async with aiohttp.ClientSession().get(self.api_url, headers=self._headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    self._quote_of_day = data["contents"]["quotes"][0]["quote"]
                    self._author_of_day = data["contents"]["quotes"][0]["author"]
                    self._last_requested = datetime.datetime.utcnow()

        return {'quote': self._quote_of_day, 'author': self._author_of_day}
