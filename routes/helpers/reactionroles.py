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


@check_permission(permission_level=DEVELOPER)
async def add_reaction_role_message(requestor: Requestor, message_id: int) -> dict:
    """Add a message id as a reaction role message."""
    is_int64(message_id)
    return await self.db.execute("SELECT public.addreactionrole($1)", message_id)


@check_permission(permission_level=DEVELOPER)
async def get_reaction_role_messages(requestor: Requestor) -> dict:
    """Get all reaction role messages."""
    return await self.db.fetch("SELECT * FROM public.getreactionroles")
