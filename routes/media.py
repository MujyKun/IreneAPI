import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

media = PintBlueprint("media", __name__, url_prefix="/media/")


@media.route("<int:media_id>")
@media.doc(
    params={
        "media_id": "Media ID to manage.",
    }
)
class Media(Resource):
    async def get(self, media_id: int):
        """Get a media.

        Use this route to get a media.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_media(requestor, media_id)

    async def delete(self, media_id: int):
        """Delete a media.

        Use this route to delete a media. This will cascade all objects dependent on the media and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_media(requestor, media_id)

    async def post(self, media_id: int):
        """Update media difficulty.

        Use this route to update media difficulty.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.upsert_media_difficulty(
            requestor,
            media_id,
            failed_guesses=request.args["failed_guesses"],
            correct_guesses=request.args["correct_guesses"],
        )


@media.route("")
@media.doc()
class Medias(Resource):
    async def get(self):
        """Get all medias.

        Use this route to get all medias.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_all_media(requestor)

    async def post(self):
        """Add a media.

        Use this route to add a media.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_media(
            requestor,
            link=request.args.get("link"),
            faces=request.args.get("faces"),
            file_type=request.args.get("file_type"),
            affiliation_id=request.args.get("affiliation_id"),
            enabled=request.args.get("enabled"),
            is_nsfw=request.args.get("is_nsfw"),
        )
