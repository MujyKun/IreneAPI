from typing import Optional
from models import Requestor, DbConnection
from functools import wraps
from .errors import LackingPermissions


permission_levels = {
    -1: 'God',
    0: 'Owner',
    1: 'Developer',
    2: 'Super Patron',
    3: 'Friend',
}


def check_permission(permission_level):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Check permission level matches the requirement.
            requestor = kwargs.get('requestor') or args[0]
            if isinstance(requestor, Requestor):
                if requestor.permission_level <= permission_level:
                    # approved access
                    return await func(*args, **kwargs)
            raise LackingPermissions
        return wrapper
    return decorator


db: Optional[DbConnection] = None


class DB:
    def __init__(self):
        self.db: Optional[DbConnection] = None


self = DB()

from .api import add_token, get_token, get_permission_level


