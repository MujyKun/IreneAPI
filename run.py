# noinspection PyUnresolvedReferences, PyPackageRequirements
from asyncio import get_event_loop
from quart import Quart, render_template, Response
from models import PgConnection
# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.drive import get_file_type, download_media
from resources.keys import postgres_options, api_port
from routes.groupmembers import groupmembers
from routes.user import user
from ws import websocket_blueprint
from routes.helpers.errors import BaseError

app = Quart(__name__)

app.register_blueprint(groupmembers)
app.register_blueprint(websocket_blueprint)
app.register_blueprint(user)

db = PgConnection(**postgres_options)


@app.errorhandler(BaseError)
async def handle_custom(error):
    return Response(response=str(error), status=error.status_code, content_type="application/json")


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
