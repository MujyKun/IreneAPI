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

personalias = PintBlueprint("personalias", __name__, url_prefix="/personalias/")


@personalias.route("<int:person_alias_id>")
@personalias.doc(
    params={
        "person_alias_id": "PersonAlias ID to manage.",
    }
)
class PersonAlias(Resource):
    async def get(self, person_alias_id: int):
        """Get a person alias.

        Use this route to get a person alias.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_person_alias(requestor, person_alias_id)

    async def delete(self, person_alias_id: int):
        """Delete a person alias.

        Use this route to delete a person alias. This will cascade all objects dependent on the person alias and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_person_alias(requestor, person_alias_id)


@personalias.route("")
@personalias.doc()
class PersonAliases(Resource):
    async def get(self):
        """Get all person aliases.

        Use this route to get all person aliases.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_person_aliases(requestor)

    async def post(self):
        """Add a person alias.

        Use this route to add a person alias.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_person_alias(
            requestor,
            alias=request.args.get("alias"),
            person_id=request.args.get("person_id"),
            guild_id=request.args.get("guild_id"),
        )
