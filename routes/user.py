from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.user

user = PintBlueprint("user", __name__, url_prefix="/user/")


@user.route("ban_user/<int:user_id>")
@user.doc(params={"user_id": "User ID to ban."})
class BanUser(Resource):
    async def post(self, user_id: int):
        """Ban A User

        Use this route to ban a user from the bot.
        """
        requestor = await login(request.headers)
        await routes.helpers.user.ban_user(requestor, user_id)


@user.route("unban_user/<int:user_id>")
@user.doc(params={"user_id": "User ID to ban."})
class UnbanUser(Resource):
    async def post(self, user_id: int):
        """Unban A User

        Use this route to unban a user from the bot.
        """
        requestor = await login(request.headers)
        await routes.helpers.user.unban_user(requestor, user_id)
