import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.reactionroles as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

reaction_roles = PintBlueprint(
    "reaction_roles", __name__, url_prefix="/reaction_roles/"
)


@reaction_roles.route("")
@reaction_roles.doc()
class RoleMessages(Resource):
    async def get(self):
        """Get all role messages."""
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_reaction_role_messages(requestor)


@reaction_roles.route("<int:message_id>")
@reaction_roles.doc(params={"message_id": "Message ID for a Reaction Role Message."})
class RoleMessagesAdd(Resource):
    async def post(self, message_id):
        """Add a Role Message."""
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_reaction_role_message(requestor, message_id)
