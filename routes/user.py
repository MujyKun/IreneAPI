from quart import Blueprint, request
from . import login
from routes.helpers.errors import InvalidLogin
import routes.helpers.user

user = Blueprint('user', __name__, url_prefix="/user")


@user.post('ban_user/<user_id>')
async def ban_user(user_id: int):
    requestor = await login(request.headers)
    await routes.helpers.user.ban_user(requestor, user_id)


@user.post('unban_user/<user_id>')
async def unban_user(user_id: int):
    requestor = await login(request.headers)
    await routes.helpers.user.unban_user(requestor, user_id)

