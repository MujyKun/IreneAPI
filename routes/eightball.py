from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.eightball as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

eight_ball = PintBlueprint("8ball", __name__, url_prefix="/8ball/")


@eight_ball.route("<int:response_id>")
@eight_ball.doc(
    params={
        "response_id": "Response ID to manage.",
    }
)
class EightBallResponse(Resource):
    async def get(self, response_id: int):
        """Get a response.

        Use this route to get a response.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_response(requestor, response_id)

    async def delete(self, response_id: int):
        """Delete a response.

        Use this route to delete a response. This will cascade all objects dependent on the response and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_response(requestor, response_id)


@eight_ball.route("")
@eight_ball.doc()
class EightBall(Resource):
    async def get(self):
        """Get all responses.

        Use this route to get all responses.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_responses(requestor)

    async def post(self):
        """Add a response.

        Use this route to add a response.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_response(requestor, request.args.get("response"))
