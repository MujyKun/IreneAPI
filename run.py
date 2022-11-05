# noinspection PyUnresolvedReferences, PyPackageRequirements
from asyncio import get_event_loop

from quart import Quart, render_template, Response, make_response
from models import PgConnection

# noinspection PyUnresolvedReferences, PyPackageRequirements
from resources.keys import postgres_options, api_port
from resources import drive

from ws import websocket_blueprint
from routes import blueprints as _blueprints, cors_handler
from routes.helpers.errors import BaseError
from quart_openapi import Swagger
from quart_cors import cors
from models import Pint


app = Pint(__name__, title="IreneAPI", contact_email="mujy@irenebot.com", version="2.0")
app = cors(app)
swagger = Swagger(app)
blueprints = _blueprints + [websocket_blueprint]  # do not override.

# print(app.config['SERVER_NAME'])
# app.config['SERVER_NAME'] = "api.irenebot.com"
for blueprint in blueprints:
    app.register_blueprint(blueprint)

db = PgConnection(**postgres_options)


@app.errorhandler(BaseError)
# @crossdomain(origin=individual_route_cross_domain_origin)
async def handle_custom(error):
    # handler = await cors_handler(swagger.as_dict)
    handler = await cors_handler(make_response)
    response = await handler(str(error), error.status_code)
    response.content_type = "application/json"
    return response


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
    handler = await cors_handler(swagger.as_dict)
    return await handler()


@app.route("/")
async def index():
    handler = await cors_handler(render_template)
    return await handler("index.html")


async def create_first_user_token():
    """create first user token for usage."""
    from routes.helpers.api import add_token
    from routes.helpers import GOD, OWNER, Requestor
    god_requestor = Requestor(-1, GOD)
    user_id = 169401247374376960  # change accordingly.
    private_token = "private_key"  # change accordingly.
    await add_token(requestor=god_requestor, user_id=user_id, unhashed_token=private_token, access_id=OWNER.id)

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

    # loop.run_until_complete(app.run_task(port=api_port))

    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    config = Config()
    config.bind = f"127.0.0.1:{api_port}"
    loop.run_until_complete(serve(app, config))
except KeyboardInterrupt:
    # cancel all tasks lingering
    ...
except Exception as e:
    print(f"{e}")
finally:
    ...
    # loop.close()
