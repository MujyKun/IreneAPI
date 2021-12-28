from quart import render_template

from quart import Blueprint

groupmembers = Blueprint("groupmembers", __name__)


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
