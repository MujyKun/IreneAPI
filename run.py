# noinspection PyUnresolvedReferences, PyPackageRequirements
from asyncio import get_event_loop

from quart import render_template, make_response, redirect, session, jsonify
from models import PgConnection

# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.keys import (
    postgres_options,
    api_port,
    support_server_link,
    bot_invite_link,
    patreon_url,
    github_url,
    signing_key,
    bot_website
)
from resources import drive

from ws import websocket_blueprint
from routes import blueprints as _blueprints
from routes.helpers.errors import BaseError
from quart_openapi import Swagger, Pint
from quart_cors import cors


app = Pint(__name__, title="IreneAPI", contact_email="mujy@irenebot.com", version="2.0")
swagger = Swagger(app)
blueprints = _blueprints + [websocket_blueprint]  # do not override.

for blueprint in blueprints:
    app.register_blueprint(blueprint)

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_DOMAIN=".irenebot.com"
)

app.secret_key = signing_key

app = cors(app, allow_origin=[bot_website.rstrip('/'), "http://127.0.0.1:5173", "localhost"], allow_credentials=True,
           allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])


db = PgConnection(**postgres_options)


@app.errorhandler(BaseError)
async def handle_custom(error):
    return jsonify({"error": str(error)}, error.status_code)


@app.route("/docs")
async def docs():
    # Global Security
    """
    components:
      securitySchemes:
        Bearer Token:
          name: Authorization
          type: apiKey
          in: header
          description: 'Make sure the API key/token is preceded by "Bearer" when passed in. '
        User ID:
          name: user_id
          type: apiKey
          in: query
          description: ''
    security:
      - Bearer Token: []
      - User ID: []
    """
    return jsonify(swagger.as_dict())


@app.route("/")
async def index():
    from routes.discord import Login, helper
    access_token = await helper.get_access_token()
    if not access_token:
        return await Login().get()
    else:
        return await render_template("index.html")


@app.route("/discord")
async def support_server_redirect():
    return redirect(support_server_link)


@app.route("/invite")
async def invite_bot_redirect():
    return redirect(bot_invite_link)


@app.route("/patreon")
async def patreon_redirect():
    return redirect(patreon_url)


@app.route("/github")
async def github_redirect():
    return redirect(github_url)


@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route("/commands")
async def commands():
    from routes.helpers.bot import get_commands
    from routes.helpers import GOD, Requestor

    return await get_commands(Requestor(0, GOD))


async def create_first_user_token():
    """create first user token for usage."""
    from routes.helpers.api import add_token
    from routes.helpers import GOD, OWNER, Requestor, add_user

    god_requestor = Requestor(-1, GOD)
    user_id = 169401247374376960  # change accordingly.
    await add_user(requestor=god_requestor, user_id=user_id)
    private_token = "private_key"  # change accordingly.
    await add_token(
        requestor=god_requestor,
        user_id=user_id,
        unhashed_token=private_token,
        access_id=OWNER.id,
    )


# if __name__ == '__main__':

loop = get_event_loop()
try:
    # instantiate google drive
    loop.run_until_complete(drive.create())

    # update helper usage of the DB.
    from routes import self

    self.db = db

    # connect to db.
    loop.run_until_complete(db.connect())

    # loop.run_until_complete(create_first_user_token())

    loop.run_until_complete(app.run_task(port=api_port))

    # from hypercorn.config import Config
    # from hypercorn.asyncio import serve
    #
    # config = Config()
    # config.bind = f"127.0.0.1:{api_port}"
    # loop.run_until_complete(serve(app, config))
except KeyboardInterrupt:
    # cancel all tasks lingering
    ...
except Exception as e:
    print(f"{e}")
finally:
    ...
    # loop.close()
