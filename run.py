# noinspection PyUnresolvedReferences, PyPackageRequirements
from asyncio import get_event_loop, run as asyncio_run
from quart import Quart, render_template, Response
from models import PgConnection

# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.keys import postgres_options, api_port
from resources import drive

from ws import websocket_blueprint
from routes import (
    affiliation,
    bloodtype,
    company,
    date,
    display,
    fandom,
    group,
    groupalias,
    guild,
    location,
    media,
    name,
    person,
    personalias,
    position,
    social,
    tag,
    twitter,
    channel,
    user,
    guessinggame,
    user_status,
    twitch,
    unscramblegame,
    wolfram,
    biasgame,
)
from routes.helpers.errors import BaseError
from quart_openapi import Pint, Resource
from quart_openapi import Swagger
from resources.twitter import Twitter

app = Pint(__name__, title="IreneAPI", contact_email="mujy@irenebot.com", version="2.0")
swagger = Swagger(app)


blueprints = [
    affiliation,
    bloodtype,
    company,
    date,
    display,
    fandom,
    group,
    groupalias,
    guild,
    location,
    media,
    name,
    person,
    personalias,
    position,
    social,
    tag,
    twitter,
    channel,
    user,
    guessinggame,
    user_status,
    unscramblegame,
    twitch,
    wolfram,
    biasgame,
    websocket_blueprint,
]

# print(app.config['SERVER_NAME'])
# app.config['SERVER_NAME'] = "api.irenebot.com"
for blueprint in blueprints:
    app.register_blueprint(blueprint)

db = PgConnection(**postgres_options)


@app.errorhandler(BaseError)
async def handle_custom(error):
    return Response(
        response=str(error), status=error.status_code, content_type="application/json"
    )


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
    return swagger.as_dict()


@app.route("/")
async def index():
    return await render_template("index.html")


if __name__ == "__main__":
    loop = get_event_loop()
    try:

        try:
            """TWITTER TESTS"""
            twitter = Twitter()
            req = twitter.get_user_id("mujykun")
            # req = twitter.me()
            # req = twitter.get_user_timeline(username="mujykun")
            tweet = loop.run_until_complete(req)
            print(tweet)
        except Exception as e:
            print(e)

        # connect to db.
        loop.run_until_complete(db.connect())

        # update helper usage of the DB.
        from routes import self

        self.db = db

        # create first user token for usage.
        from routes.helpers.api import add_token
        from routes.helpers import GOD, OWNER, Requestor

        god_requestor = Requestor(-1, GOD)

        user_id = 169401247374376960
        private_token = "private_key"  # change accordingly.
        # loop.run_until_complete(add_token(requestor=god_requestor, user_id=user_id, unhashed_token=private_token, access_id=OWNER.id))

        # instantiate google drive
        loop.run_until_complete(drive.create())

        # loop.run_until_complete(app.run_task(port=api_port))
        # from hypercorn.config import Config
        # from hypercorn.asyncio import serve
        #
        # config = Config()
        # config.bind = f"127.0.0.1:{api_port}"
        # asyncio_run(serve(app, config))

    except KeyboardInterrupt:
        # cancel all tasks lingering
        ...
    finally:
        loop.close()
