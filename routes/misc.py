import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.misc as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

urban = PintBlueprint("urban", __name__, url_prefix="/urban/")


@urban.route("/")
@urban.doc(
)
class Urban(Resource):
    async def post(self):
        """Get a definition from UrbanDictionary.

        Use this route to get the definitions of a phrase from UrbanDictionary
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_urban_definitions(requestor, phrase=request.args.get("phrase"))
