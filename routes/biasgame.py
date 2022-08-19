from quart import request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.biasgame as helper

biasgame = PintBlueprint("biasgame", __name__, url_prefix="/biasgame/")


@biasgame.route("generate_pvp")
@biasgame.doc()
class BiasGame(Resource):
    async def post(self):
        """Generate a PvP image.

        Use this route to generate a PvP image.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.generate_pvp(
            requestor,
            request.args.get("first_image_url"),
            request.args.get("second_image_url"),
        )


@biasgame.route("winners")
@biasgame.doc()
class BiasGameWinner(Resource):
    async def post(self):
        """Get the winners for a user.

        Use this route to get the winners of all bias games for a user.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_winners(
            requestor, request.args.get("user_id"), request.args.get("limit") or 15
        )

    async def put(self):
        """Increment a win for a user's bias game.

        Use this route to increment a win in the bias game.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.upsert_wins(
            requestor, request.args.get("user_id"), request.args.get("person_id")
        )


@biasgame.route("generate_bracket")
@biasgame.doc()
class BiasGameBracket(Resource):
    async def post(self):
        """Generate a PvP bracket.

        Use this route to generate a PvP bracket.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.generate_bracket(requestor, request.args.get("game_info"))
