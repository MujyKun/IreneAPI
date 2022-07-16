from . import (
    self,
    check_permission,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
    is_int64,
)
from models import Requestor


@check_permission(permission_level=DEVELOPER)
async def get_languages(requestor: Requestor):
    return await self.db.fetch("SELECT * FROM public.getlanguages")
