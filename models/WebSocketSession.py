class WebSocketSession:
    """An active WebSocket Session."""
    def __init__(self, user_id, permission_level):
        self.user_id = user_id
        self.permission_level = permission_level