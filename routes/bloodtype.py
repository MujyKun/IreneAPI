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

bloodtype = PintBlueprint("bloodtype", __name__, url_prefix="/bloodtype/")


@bloodtype.route("<int:bloodtype_id>")
@bloodtype.doc(
    params={
        "bloodtype_id": "BloodType ID to manage.",
    }
)
class BloodType(Resource):
    async def get(self, bloodtype_id: int):
        """Get a bloodtype.

        Use this route to get a bloodtype.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_blood_type(requestor, bloodtype_id)

    async def delete(self, bloodtype_id: int):
        """Delete a bloodtype.

        Use this route to delete a bloodtype. This will cascade all objects dependent on the bloodtype and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_blood_type(requestor, bloodtype_id)


@bloodtype.route("")
@bloodtype.doc()
class BloodTypes(Resource):
    async def get(self):
        """Get all bloodtypes.

        Use this route to get all bloodtypes.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_blood_types(requestor)

    async def post(self):
        """Add a bloodtype.

        Use this route to add a bloodtype.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_blood_type(requestor, request.args.get("name"))
