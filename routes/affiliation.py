import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

affiliation = PintBlueprint("affiliation", __name__, url_prefix="/affiliation/")


@affiliation.route("<int:affiliation_id>")
@affiliation.doc(
    params={
        "affiliation_id": "Affiliation ID to manage.",
    }
)
class Affiliation(Resource):
    async def get(self, affiliation_id: int):
        """Get an affiliation.

        Use this route to get an affiliation.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_affiliation(requestor, affiliation_id)

    async def delete(self, affiliation_id: int):
        """Delete an affiliation.

        Use this route to delete an affiliation. This will cascade all objects dependent on the affiliation and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_affiliation(requestor, affiliation_id)


@affiliation.route("")
@affiliation.doc()
class Affiliations(Resource):
    async def get(self):
        """Get all affiliations.

        Use this route to get all affiliations.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_affiliations(requestor)

    async def post(self):
        """Add an affiliation.

        Use this route to add an affiliation.
        """
        requestor = await login(headers=request.headers, data=request.args)
        person_id = request.args.get("person_id")
        group_id = request.args.get("group_id")
        position_ids = request.args.get("position_ids")
        stage_name = request.args.get("stage_name")
        return await helper.add_affiliation(
            requestor, person_id, group_id, position_ids, stage_name
        )
