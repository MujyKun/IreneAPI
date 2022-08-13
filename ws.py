from quart import Blueprint, websocket

from routes import connected_websockets, login
from routes.helpers import helper_routes
from models import WebSocketSession
from routes.helpers.errors import BadRequest

websocket_blueprint = Blueprint("ws", __name__)


@websocket_blueprint.websocket("/ws")
async def ws():
    """Create a WebSocket connection."""
    wss = await login(websocket.headers, data=websocket.args, handle_websocket=True)

    if not wss:
        # failed to log in.
        return

    await websocket.accept()

    try:
        while True:
            # client must send in their requests.
            data = await websocket.receive_json()
            result = await process_ws_data(socket=wss, data=data)
            await websocket.send_json(result)
    except Exception as e:
        print(e)

    # remove the current websocket.
    existing_ws = connected_websockets.get(wss.user_id)
    if len(existing_ws) > 1:
        existing_ws.pop(wss.wss_id)
    else:
        connected_websockets.pop(wss.user_id)


async def process_ws_data(socket: WebSocketSession, data: dict) -> dict:
    """Process the data coming from a websocket."""
    response = dict()

    try:
        # mark the callback id
        callback_id = data.get("callback_id")
        if callback_id:
            response["callback_id"] = callback_id
            data.pop("callback_id")

        route = data["route"]
        # Add a slash to the end of the route if it's only the blueprint keyword.
        # we know it's a main/single route if there is no slash in the route at all.
        if "/" not in route:
            route += "/"

        method: str = (data["method"]).upper()
        search_method = f"{route}.{method}"
        helper = helper_routes[search_method]

        # required arguments
        helper_function_args = dict()
        for param in helper["params"]:
            if param == "requestor":
                helper_function_args["requestor"] = socket
                continue
            helper_function_args[param] = data[param]

        if len(helper["params"]) != len(helper_function_args):
            raise BadRequest(callback_id)

        # optional arguments
        optional_params = helper.get("optional")
        if optional_params:
            for param in helper["optional"]:
                if data.get(param) is not None:
                    helper_function_args[param] = data[param]

        # NOTE: we will not raise a bad request for problems with optional parameters.
        # breakpoint()
        result = await helper["function"](**helper_function_args)

        if not result:
            result = dict({"results": None})

        result["callback_id"] = callback_id
        return result
    except Exception as e:
        print(e)
        response["error"] = f"{e}"
        response["results"] = None

    return response
