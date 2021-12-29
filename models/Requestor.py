from routes.helpers import Access


class Requestor:
    def __init__(self, user_id: int, permission_level: Access):
        self.user_id = user_id
        self.access: Access = permission_level
