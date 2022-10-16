import aiohttp


class Urban:
    def __init__(self):
        from . import keys

        self._base_url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        self._headers = {'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
                         'x-rapidapi-key': keys.urban_key}
        self.session = aiohttp.ClientSession()

    async def query(self, phrase):
        query_string = {"term": f"{phrase}"}
        async with self.session.get(self._base_url, headers=self._headers, params=query_string) as r:
            data = await r.json()
            return data
