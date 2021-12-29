from . import Requestor, Access

session_identifier = -1


# Since a single user can have multiple sessions, this incremented variable will be a session's unique identifier.


class WebSocketSession(Requestor):
    """An active WebSocket Session."""

    def __init__(self, user_id, permission_level: Access):
        super(WebSocketSession, self).__init__(user_id, permission_level)
        global session_identifier
        session_identifier += 1
        self.wss_id = session_identifier
