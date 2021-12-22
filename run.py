# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.keys import private_keys, idol_folder, top_gg_webhook_key, bot_invite_link, patreon_url, \
    postgres_options, api_port
# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.drive import get_file_type, download_media
from models import PgConnection, check_hashed_token, WebSocketSession
from functools import partial, wraps
from quart import Quart, render_template, websocket
from asyncio import get_event_loop, Queue

from routes.groupmembers import groupmembers

app = Quart(__name__)

app.register_blueprint(groupmembers)

db = PgConnection(**postgres_options)

connected_websockets = set()

@app.route('/')
async def index():
    return await render_template('index.html')


async def login(login_headers, handle_websocket=True):
    error_reason = "Failed to Authenticate."
    error_code = 401
    try:
        token = login_headers['Authorization']
        user_id = int(login_headers['user_id'])
        expected_token = await db.get_token(user_id)

        if not expected_token:
            raise Exception("Bad Request")

        login_success = check_hashed_token(token, expected_token)

        if not login_success:
            error_reason += "Token does not match the user."
        else:
            if handle_websocket:
                permission_level = await db.get_permission_level(user_id)
                connected_websockets.add(WebSocketSession(user_id, permission_level))
            return True
    except KeyError:
        error_reason += f"You are missing headers from your request. Please follow the documentation for login at {'...'}"
    except Exception as e:
        error_code = 400
        error_reason = "Bad Request"

    if handle_websocket:
        await websocket.close(code=error_code, reason=error_reason)
    return False


async def process_data(data) -> dict:

    return dict({'test': 'test'})


@app.websocket('/ws')
async def ws():
    if not await login(websocket.headers):
        # failed to log in.
        return

    await websocket.accept()

    while True:
        # client must send in their requests.
        data = await websocket.receive()

        result = await process_data(data)
        await websocket.send_json(result)

if __name__ == "__main__":
    loop = get_event_loop()
    try:
        # connect to db.
        loop.run_until_complete(db.connect())
        loop.run_until_complete(app.run_task(port=api_port))
    except KeyboardInterrupt:
        ...
        # loop.run_until_complete(self.close())
        # cancel all tasks lingering
    finally:
        loop.close()
