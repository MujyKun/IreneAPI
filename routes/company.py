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

company = PintBlueprint("company", __name__, url_prefix="/company/")


@company.route("<int:company_id>")
@company.doc(
    params={
        "company_id": "Company ID to manage.",
    }
)
class Company(Resource):
    async def get(self, company_id: int):
        """Get a company.

        Use this route to get a company.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_company(requestor, company_id)

    async def delete(self, company_id: int):
        """Delete a company.

        Use this route to delete a company. This will cascade all objects dependent on the company and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_company(requestor, company_id)


@company.route("")
@company.doc()
class Companies(Resource):
    async def get(self):
        """Get all companies.

        Use this route to get all companies.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_companies(requestor)

    async def post(self):
        """Add a company.

        Use this route to add a company.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_company(
            requestor,
            name=request.args.get("name"),
            description=request.args.get("description"),
            date_id=request.args.get("date_id"),
        )
