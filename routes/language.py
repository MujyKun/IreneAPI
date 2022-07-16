import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.language as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

language = PintBlueprint("guild", __name__, url_prefix="/language/")


@language.route("")
@language.doc()
class Language(Resource):
    async def get(self):
        """Get all languages with their packs."""
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_languages(requestor)
