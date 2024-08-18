import asyncio
from typing import Union

from quart import Blueprint, request, redirect, jsonify
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.discord as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD
from resources.keys import discord_auth_url

discord = PintBlueprint("discord", __name__, url_prefix="/discord/")


@discord.route("login")
class Login(Resource):
    async def get(self):
        """Redirect to oauth page.

        Use this route to redirect to oauth page.
        """
        fallback_url = request.args.get("state")
        path = discord_auth_url + f'&state={fallback_url}' if fallback_url else discord_auth_url
        return redirect(path)


@discord.route("callback")
class LoginCallback(Resource):
    async def get(self):
        """
        Handle the callback process from Discord.

        This route should only be called by discord.
        """
        code = request.args.get("code")
        fallback_url = request.args.get("state")
        if not code:
            return jsonify({"error": "Missing code parameter"}), 400
        return await helper.handle_discord_login(code, fallback_url=fallback_url)


@discord.route("user")
class InfoAboutMe(Resource):
    async def get(self):
        return await helper.get_user_info()


