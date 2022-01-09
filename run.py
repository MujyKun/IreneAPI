# noinspection PyUnresolvedReferences, PyPackageRequirements
from asyncio import get_event_loop
from quart import Quart, render_template, Response
from models import PgConnection

# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.keys import postgres_options, api_port
from resources import drive
from routes.groupmembers import groupmembers
from routes.user import user
from routes.twitter import twitter
from routes.channel import channel
from ws import websocket_blueprint
from routes.helpers.errors import BaseError
from quart_openapi import Pint, Resource
from quart_openapi import Swagger
from resources.twitter import Twitter

app = Pint(__name__, title="IreneAPI", contact_email="mujy@irenebot.com", version="2.0")
swagger = Swagger(app)

# print(app.config['SERVER_NAME'])
# app.config['SERVER_NAME'] = "api.irenebot.com"
app.register_blueprint(twitter)
app.register_blueprint(groupmembers)
app.register_blueprint(websocket_blueprint)
app.register_blueprint(user)
app.register_blueprint(channel)

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

        # instantiate google drive
        loop.run_until_complete(drive.create())

        loop.run_until_complete(app.run_task(port=api_port))

    except KeyboardInterrupt:
        # cancel all tasks lingering
        ...
    finally:
        loop.close()
