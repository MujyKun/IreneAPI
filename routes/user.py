import asyncio

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.user as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

user = PintBlueprint("user", __name__, url_prefix="/user/")


@user.route("")
@user.doc()
class Users(Resource):
    async def get(self, user_id: int):
        """Get the information about all users

        Use this route to get all user information. A login is still needed.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_all_users(requestor, user_id)


@user.route("<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the status of."})
class UserStatus(Resource):
    async def get(self, user_id: int):
        """Get the information about a user.

        Use this route to get a user's information. A login is still needed.
        Pass in a user id of 0 to get all users.
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

        Use this route to check if a user is banned. A login is NOT needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
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

        Use this route to check if a user is a patron. A login is NOT needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
        return await helper.get_user_patron(requestor, user_id)

    async def post(self, user_id: int):
        """Add a patron.

        Use this route to add the patron status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_patron(requestor, user_id)

    async def delete(self, user_id: int):
        """Unban a user.

        Use this route to remove the patron status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_patron(requestor, user_id)


@user.route("token/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the api token status of."})
class UserTokenStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user has a token.

        Use this route to check if a user has a token. A login is NOT needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
        return await api_helper.check_token_exists(requestor, user_id)

    async def post(self, user_id: int):
        """Add an api token.

        Use this route to add a token for a user.
        The unhashed token and access id must be sent in the body of the request.

        """
        requestor = await login(headers=request.headers, data=request.args)
        return await api_helper.add_token(
            requestor,
            unhashed_token=request.args.get("unhashed_token"),
            access_id=request.args.get("access_id"),
        )

    async def delete(self, user_id: int):
        """Delete a user's token.

        Use this route to remove the token that belongs of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await api_helper.delete_token(requestor, user_id)


@user.route("superpatron_status/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the super patron status of."})
class UserSuperPatronStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user is a super patron.

        Use this route to check if a user is a super patron. A login is not needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
        return await helper.get_user_super_patron(requestor, user_id)

    async def post(self, user_id: int):
        """Add a patron.

        Use this route to add the patron status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_super_patron(requestor, user_id)

    async def delete(self, user_id: int):
        """Unban a user.

        Use this route to remove the super patron status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_super_patron(requestor, user_id)


@user.route("mod_status/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the moderator status of."})
class UserModStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user is a moderator.

        Use this route to check if a user is a moderator. A login is not needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
        return await helper.get_user_mod(requestor, user_id)

    async def post(self, user_id: int):
        """Add a moderator.

        Use this route to add the moderator status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_mod(requestor, user_id)

    async def delete(self, user_id: int):
        """Remove a user as a moderator.

        Use this route to remove the moderator status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_mod(requestor, user_id)


@user.route("translator_status/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the translator status of."})
class UserTranslatorStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user is a translator.

        Use this route to check if a user is a translator. A login is not needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
        return await helper.get_user_translator(requestor, user_id)

    async def post(self, user_id: int):
        """Add a translator.

        Use this route to add the translator status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_translator(requestor, user_id)

    async def delete(self, user_id: int):
        """Remove a user as a translator.

        Use this route to remove the translator status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_translator(requestor, user_id)


@user.route("proofreader_status/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the proofreader status of."})
class UserProofreaderStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user is a proofreader.

        Use this route to check if a user is a proofreader. A login is not needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
        return await helper.get_user_proofreader(requestor, user_id)

    async def post(self, user_id: int):
        """Add a proofreader.

        Use this route to add the proofreader status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_proofreader(requestor, user_id)

    async def delete(self, user_id: int):
        """Remove a user as a proofreader.

        Use this route to remove the proofreader status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_proofreader(requestor, user_id)


@user.route("data_mod_status/<int:user_id>")
@user.doc(params={"user_id": "User ID to manage the proofreader status of."})
class UserDataModStatus(Resource):
    async def get(self, user_id: int):
        """Check if a user is a data mod.

        Use this route to check if a user is a data mod. A login is not needed.
        """
        requestor = Requestor(user_id=0, permission_level=USER)
        return await helper.get_user_data_mod(requestor, user_id)

    async def post(self, user_id: int):
        """Add a data mod.

        Use this route to add the data mod status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_data_mod(requestor, user_id)

    async def delete(self, user_id: int):
        """Remove a user as a data mod.

        Use this route to remove the data mod status of a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_data_mod(requestor, user_id)
