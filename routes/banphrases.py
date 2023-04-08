import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint
from . import Resource

from . import login
import routes.helpers.banphrases as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

ban_phrases = PintBlueprint("banphrases", __name__, url_prefix="/banphrases/")


@ban_phrases.route("<int:phrase_id>")
@ban_phrases.doc(
    params={
        "phrase_id": "Phrase ID to manage.",
    }
)
class BanPhrase(Resource):
    async def get(self, phrase_id: int):
        """Get a ban phrase.

        Use this route to get a phrase.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_ban_phrase(requestor, phrase_id)

    async def delete(self, phrase_id: int):
        """Delete a ban phrase.

        Use this route to delete a phrase. This will cascade all objects dependent on the display and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_ban_phrase(requestor, phrase_id)


@ban_phrases.route("")
@ban_phrases.doc()
class BanPhrases(Resource):
    async def get(self):
        """Get all ban phrases.

        Use this route to get all ban phrases.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_ban_phrases(requestor)

    async def post(self):
        """Add a ban phrase.

        Use this route to add a ban phrase.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_ban_phrase(
            requestor,
            guild_id=request.args.get("guild_id"),
            log_channel_id=request.args.get("log_channel_id"),
            phrase=request.args.get("phrase"),
            punishment=request.args.get("punishment"),
        )
