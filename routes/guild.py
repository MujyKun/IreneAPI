import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.guild as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

guild = PintBlueprint("guild", __name__, url_prefix="/guild/")


@guild.route("<int:guild_id>")
@guild.doc(
    params={
        "guild_id": "Guild ID to manage.",
    }
)
class Guild(Resource):
    async def get(self, guild_id: int):
        """Get a guild.

        Use this route to get a guild.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_guild(requestor, guild_id)

    async def delete(self, guild_id: int):
        """Delete a guild.

        Use this route to delete a guild. This will cascade all objects dependent on the guild and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_guild(requestor, guild_id)


@guild.route("")
@guild.doc()
class Guilds(Resource):
    async def get(self):
        """Get all guilds.

        Use this route to get all guilds.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_guilds(requestor)

    async def post(self):
        """Add a guild.

        Use this route to add a guild.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_guild(
            requestor,
            guild_id=request.args.get("guild_id"),
            name=request.args.get("name"),
            emoji_count=request.args.get("emoji_count"),
            region=request.args.get("region"),
            afk_timeout=request.args.get("afk_timeout"),
            icon=request.args.get("icon"),
            owner_id=request.args.get("owner_id"),
            banner=request.args.get("banner"),
            description=request.args.get("description"),
            mfa_level=request.args.get("mfa_level"),
            splash=request.args.get("splash"),
            nitro_level=request.args.get("nitro_level"),
            boosts=request.args.get("boosts"),
            text_channel_count=request.args.get("text_channel_count"),
            voice_channel_count=request.args.get("voice_channel_count"),
            category_count=request.args.get("category_count"),
            emoji_limit=request.args.get("emoji_limit"),
            member_count=request.args.get("member_count"),
            role_count=request.args.get("role_count"),
            shard_id=request.args.get("shard_id"),
            create_date=request.args.get("create_date"),
            has_bot=request.args.get("has_bot"),
        )
