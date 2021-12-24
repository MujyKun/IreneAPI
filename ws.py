from quart import Blueprint, websocket

from routes import connected_websockets, login

websocket_blueprint = Blueprint("ws", __name__)


@websocket_blueprint.websocket("/ws")
async def ws():
    """Create a WebSocket connection."""
    wss = await login(websocket.headers, handle_websocket=True)
    if not wss:
        # failed to log in.
        return

    await websocket.accept()

    try:
        while True:
            # client must send in their requests.
            data = await websocket.receive()

            result = await process_ws_data(data)
            await websocket.send_json(result)
    except Exception as e:
        print(e)

    # remove the current websocket.
    existing_ws = connected_websockets.get(wss.user_id)
    if len(existing_ws) > 1:
        existing_ws.pop(wss.wss_id)
    else:
        connected_websockets.pop(wss.user_id)


async def process_ws_data(data) -> dict:
    return dict({"test": "test"})
