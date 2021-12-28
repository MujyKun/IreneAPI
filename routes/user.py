import asyncio

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.user as helper

user = PintBlueprint("user", __name__, url_prefix="/user/")


@user.route("<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the status of."})
class UserStatus(Resource):
    async def get(self, user_id: int):
        """Get the information about a user.

        Use this route to get a user's information. A login is still needed.
        Pass in a user id of -1 to get all users.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_user(requestor, user_id)

    async def post(self, user_id: int):
        """Add a user.

        Use this route to add a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_user(requestor, user_id)

    async def delete(self, user_id: int):
        """Delete a user.

        Use this route to remove a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_user(requestor, user_id)


@user.route("ban_status/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the ban status of."})
class UserBanStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user is banned.

        Use this route to check if a user is banned. A login is still needed.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_user_banned(requestor, user_id)

    async def post(self, user_id: int):
        """Ban a user.

        Use this route to ban a user from the bot.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.ban_user(requestor, user_id)

    async def delete(self, user_id: int):
        """Unban a user.

        Use this route to unban a user from the bot.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.unban_user(requestor, user_id)


@user.route("patron_status/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the patron status of."})
class UserPatronStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user is a patron.

        Use this route to check if a user is a patron. A login is still needed.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_user_patron(requestor, user_id)

    async def post(self, user_id: int):
        """Add a patron.

        Use this route to add the patron status to a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_patron(requestor, user_id)

    async def delete(self, user_id: int):
        """Unban a user.

        Use this route to remove the patron status to a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_patron(requestor, user_id)
