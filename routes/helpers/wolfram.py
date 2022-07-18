from typing import List

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

from resources import wolfram as wolfram_obj


@check_permission(permission_level=SUPER_PATRON)
async def wolfram_query(requestor: Requestor, query: str) -> dict:
    """Query WolframAlpha"""
    return await wolfram_obj.query(query)
