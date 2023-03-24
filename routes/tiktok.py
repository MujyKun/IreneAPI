from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.tiktok as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

tiktok = PintBlueprint("tiktok", __name__, url_prefix="/tiktok/")


@tiktok.route("latest_video/<string:username>")
@tiktok.doc(
    params={
        "username": "Tiktok username to manage.",
    }
)
class LatestTiktok(Resource):
    async def get(self, username: str):
        """Get the latest video ID of a TikTok user.

        Use this route to get the latest video ID of a TikTok user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_latest_tiktok_video(requestor, username)


@tiktok.route("<string:username>")
@tiktok.doc(
    params={
        "username": "Tiktok username to manage.",
    }
)
class TikTokAccount(Resource):
    async def get(self, username: str):
        """Get a TikTok Account.

        Use this route to get a TikTok Account.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_tiktok_account(requestor, username)


@tiktok.route("")
@tiktok.doc()
class TikTokAccounts(Resource):
    async def get(self):
        """Get all accounts.

        Use this route to get all accounts.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_tiktok_accounts(requestor)

    async def post(self):
        """Add an account.

        Add an account
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_tiktok_account(
            requestor,
            request.args.get("username"),
            request.args.get("user_id"),
            request.args.get("channel_id"),
            request.args.get("role_id"),
        )
