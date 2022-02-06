import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

social = PintBlueprint("social", __name__, url_prefix="/social/")


@social.route("<int:social_id>")
@social.doc(
    params={
        "position_id": "Social ID to manage.",
    }
)
class Social(Resource):
    async def get(self, social_id: int):
        """Get a social.

        Use this route to get a social.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_social(requestor, social_id)

    async def delete(self, social_id: int):
        """Delete a social.

        Use this route to delete a social. This will cascade all objects dependent on the social and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_social(requestor, social_id)


@social.route("")
@social.doc()
class Socials(Resource):
    async def get(self):
        """Get all socials.

        Use this route to get all socials.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_socials(requestor)

    async def post(self, social_id: int):
        """Add a social.

        Use this route to add a social.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_social(
            requestor,
            twitter=request.args.get("twitter"),
            youtube=request.args.get("youtube"),
            melon=request.args.get("melon"),
            instagram=request.args.get("instagram"),
            vlive=request.args.get("vlive"),
            spotify=request.args.get("spotify"),
            fancafe=request.args.get("fancafe"),
            facebook=request.args.get("facebook"),
            tiktok=request.args.get("tiktok"),
        )
