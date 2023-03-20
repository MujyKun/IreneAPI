import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

groupalias = PintBlueprint("groupalias", __name__, url_prefix="/groupalias/")


@groupalias.route("<int:group_alias_id>")
@groupalias.doc(
    params={
        "group_alias_id": "GroupAlias ID to manage.",
    }
)
class GroupAlias(Resource):
    async def get(self, group_alias_id: int):
        """Get a group alias.

        Use this route to get a group alias.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_group_alias(requestor, group_alias_id)

    async def delete(self, group_alias_id: int):
        """Delete a group alias.

        Use this route to delete a group alias. This will cascade all objects dependent on the group alias and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_group_alias(requestor, group_alias_id)


@groupalias.route("")
@groupalias.doc()
class GroupAliases(Resource):
    async def get(self):
        """Get all group aliases.

        Use this route to get all group aliases.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_group_aliases(requestor)

    async def post(self):
        """Add a group alias.

        Use this route to add a group alias.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_group_alias(
            requestor,
            alias=request.args.get("alias"),
            group_id=request.args.get("person_id"),
            guild_id=request.args.get("guild_id"),
        )
