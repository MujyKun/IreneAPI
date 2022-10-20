import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.wolfram as helper
from models import Requestor

wolfram = PintBlueprint("wolfram", __name__, url_prefix="/wolfram/")


@wolfram.route("")
@wolfram.doc()
class Wolfram(Resource):
    async def post(self):
        """Query to WolframAlpha.

        Use this route to query to WolframAlpha.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.wolfram_query(requestor, request.args.get("query"))
