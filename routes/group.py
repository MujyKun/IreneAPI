import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

group = PintBlueprint("group", __name__, url_prefix="/group/")


@group.route("<int:group_id>")
@group.doc(
    params={
        "group_id": "Group ID to manage.",
    }
)
class Group(Resource):
    async def get(self, group_id: int):
        """Get a group.

        Use this route to get a group.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_group(requestor, group_id)

    async def post(self, group_id: int):
        """Add a group.

        Use this route to add a group.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_group(requestor, group_id)

    async def delete(self, group_id: int):
        """Delete a group.

        Use this route to delete a group. This will cascade all objects dependent on the group and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_group(requestor, group_id)


@group.route("")
@group.doc()
class Groups(Resource):
    async def get(self):
        """Get all groups.

        Use this route to get all groups.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_groups(requestor)


@group.route("<int:group_id>/media")
@group.doc(
    params={
        "group_id": "Group ID to get media information for.",
    }
)
class GroupMedia(Resource):
    async def get(self, group_id: int):
        """Get a list of media information that belong to a Group.

        Use this route to get a list of media information that belong to a Group.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_group_media_info(requestor, group_id)

    async def post(self, group_id: int):
        """Generate random group media that can be filtered.

        Use this route to generate random group media that can be filtered.

        """
        requestor = await login(headers=request.headers, data=request.args)
        kwargs = helper.get_media_kwargs(requestor, request.args)
        kwargs["group_id"] = group_id
        return await helper.generate_media_group(**kwargs)
