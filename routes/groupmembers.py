from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

groupmembers = Blueprint("groupmembers", __name__, url_prefix="/groupmembers/")


@groupmembers.route("/test")
async def test():
    from routes.helpers.api import add_token
    from models import Requestor

    await add_token(
        requestor=Requestor(-1, 0),
        user_id=169401247374376960,
        unhashed_token="test",
        access_id=1,
    )
    return await render_template("index.html")
