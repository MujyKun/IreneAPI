# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.keys import private_keys, idol_folder, top_gg_webhook_key, bot_invite_link, patreon_url, \
    postgres_options, api_port
# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.drive import get_file_type, download_media
from models import PgConnection
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


async def login(login_headers):
    try:
        token = login_headers['Authorization']
        user_id = login_headers['user_id']
        return True
    except KeyError:
        try:
            await websocket.close(code=401, reason=f"You are missing headers from your request."
                                                   f"Please follow the documentation for login at {'...'}")
        except:
            ...
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
