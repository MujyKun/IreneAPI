from . import (
    self,
    check_permission,
    is_int64,
    GOD,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
)
from models import Requestor
from resources import urban


@check_permission(permission_level=SUPER_PATRON)
async def get_urban_definitions(requestor: Requestor, phrase: str) -> dict:
    """Get urban dictionary definitions."""
    return await urban.query(phrase)

