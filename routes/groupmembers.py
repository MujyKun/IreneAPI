from quart import render_template

from quart import Blueprint

groupmembers = Blueprint("groupmembers", __name__)


@groupmembers.route("/test")
async def test():
    return await render_template("index.html")
