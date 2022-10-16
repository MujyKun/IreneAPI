import aiohttp


class Urban:
    def __init__(self):
        from . import keys

        self._headers = keys.urban_key
        self.url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        self.session = aiohttp.ClientSession()

    async def query(self, phrase):
        query_string = {"term": f"{phrase}"}
        async with self.session.get(
            self.url, headers=self._headers, params=query_string
        ) as r:
            return await r.json()
