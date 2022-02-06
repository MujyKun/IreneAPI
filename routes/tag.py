import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

tag = PintBlueprint("tag", __name__, url_prefix="/tag/")


@tag.route("<int:tag_id>")
@tag.doc(
    params={
        "tag_id": "Tag ID to manage.",
    }
)
class Tag(Resource):
    async def get(self, tag_id: int):
        """Get a tag.

        Use this route to get a tag.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_tag(requestor, tag_id)

    async def delete(self, tag_id: int):
        """Delete a tag.

        Use this route to delete a tag. This will cascade all objects dependent on the tag and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_tag(requestor, tag_id)


@tag.route("")
@tag.doc()
class Tags(Resource):
    async def get(self):
        """Get all tags.

        Use this route to get all tags.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_tags(requestor)

    async def post(self):
        """Add a tag.

        Use this route to add a tag.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_tag(requestor, request.args.get("name"))
