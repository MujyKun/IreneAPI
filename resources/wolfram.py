import aiohttp
import xmltodict


class Wolfram:
    def __init__(self):
        from . import keys

        self.app_id = keys.wolfram_app_id
        self.session = aiohttp.ClientSession()

    async def query(self, query):
        query_link = (
            f"http://api.wolframalpha.com/v2/query?input={query}&appid={self.app_id}"
        )
        async with self.session.get(query_link) as r:
            xml_data = await r.content.read()
            dict_content = (xmltodict.parse(xml_data)).get("queryresult")
            return {"results": dict_content}
