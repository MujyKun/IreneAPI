# noinspection PyUnresolvedReferences, PyPackageRequirements
from asyncio import get_event_loop
from quart import Quart, render_template
from models import PgConnection
# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.drive import get_file_type, download_media
from resources.keys import postgres_options, api_port
from routes.groupmembers import groupmembers
from ws import websocket_blueprint

app = Quart(__name__)

app.register_blueprint(groupmembers)
app.register_blueprint(websocket_blueprint)

db = PgConnection(**postgres_options)


@app.route('/')
async def index():
    return await render_template('index.html')


if __name__ == "__main__":
    loop = get_event_loop()
    try:
        # connect to db.
        loop.run_until_complete(db.connect())

        # update helper usage of the DB.
        from routes import self
        self.db = db

        loop.run_until_complete(app.run_task(port=api_port))
    except KeyboardInterrupt:
        # cancel all tasks lingering
        ...
    finally:
        loop.close()
