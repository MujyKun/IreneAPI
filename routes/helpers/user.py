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
async def get_user(requestor: Requestor, user_id: int) -> dict:
    """Get a user's information if they exist.

    Pass in the user id as 0 to get all users.
    """
    is_int64(user_id)
    if user_id == 0:
        return await self.db.fetch("SELECT * FROM public.getusers")
    return await self.db.fetch_row("SELECT * FROM public.getuser($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def add_user(requestor: Requestor, user_id: int) -> dict:
    """Add a user."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.adduser($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_user(requestor: Requestor, user_id: int) -> dict:
    """Delete a user."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.deleteuser($1)", user_id)


@check_permission(permission_level=USER)
async def get_user_banned(requestor: Requestor, user_id: int) -> dict:
    """Check if a user is banned."""
    is_int64(user_id)
    return await self.db.fetch_row("SELECT public.getbanstatus($1)", user_id)


@check_permission(permission_level=USER)
async def get_user_translator(requestor: Requestor, user_id: int) -> dict:
    """Check if a user is a translator."""
    is_int64(user_id)
    return await self.db.fetch_row("SELECT public.gettranslatorstatus($1)", user_id)


@check_permission(permission_level=USER)
async def get_user_proofreader(requestor: Requestor, user_id: int) -> dict:
    """Check if a user is a proofreader."""
    is_int64(user_id)
    return await self.db.fetch_row("SELECT public.getproofreaderstatus($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def ban_user(requestor: Requestor, user_id: int) -> dict:
    """Ban a user."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.botban($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def unban_user(requestor: Requestor, user_id: int) -> dict:
    """Unban a user."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.botunban($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def add_patron(requestor: Requestor, user_id: int) -> dict:
    """Add a patron."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.addpatron($1)", user_id)


@check_permission(permission_level=USER)
async def get_user_patron(requestor: Requestor, user_id: int) -> dict:
    """Check if the user is a patron."""
    is_int64(user_id)
    return await self.db.fetch_row("SELECT public.getpatronstatus($1)", user_id)


@check_permission(permission_level=USER)
async def get_user_data_mod(requestor: Requestor, user_id: int) -> dict:
    """Check if the user is a data moderator."""
    is_int64(user_id)
    return await self.db.fetch_row("SELECT public.getdatamodstatus($1)", user_id)


@check_permission(permission_level=USER)
async def get_user_super_patron(requestor: Requestor, user_id: int) -> dict:
    """Check if the user is a super patron."""
    is_int64(user_id)
    return await self.db.fetch_row("SELECT public.getsuperpatronstatus($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def add_super_patron(requestor: Requestor, user_id: int) -> dict:
    """Add a super patron."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.addsuperpatron($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def add_data_mod(requestor: Requestor, user_id: int) -> dict:
    """Add a data moderator."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.adddatamod($1)", user_id)


@check_permission(permission_level=USER)
async def get_user_mod(requestor: Requestor, user_id: int) -> dict:
    """Check if a user is a moderator."""
    is_int64(user_id)
    return await self.db.fetch_row("SELECT public.getmodstatus($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def add_mod(requestor: Requestor, user_id: int) -> dict:
    """Add a moderator."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.addmod($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def add_proofreader(requestor: Requestor, user_id: int) -> dict:
    """Add a proofreader."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.addproofreader($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def add_translator(requestor: Requestor, user_id: int) -> dict:
    """Add a translator."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.addtranslator($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_patron(requestor: Requestor, user_id: int) -> dict:
    """Delete a patron."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.deletepatron($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_super_patron(requestor: Requestor, user_id: int) -> dict:
    """Delete a super patron."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.deletesuperpatron($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_data_mod(requestor: Requestor, user_id: int) -> dict:
    """Delete a data moderator."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.deletedatamod($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_mod(requestor: Requestor, user_id: int) -> dict:
    """Delete a moderator."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.deletemod($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_proofreader(requestor: Requestor, user_id: int) -> dict:
    """Delete a proofreader."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.deleteproofreader($1)", user_id)


@check_permission(permission_level=DEVELOPER)
async def delete_translator(requestor: Requestor, user_id: int) -> dict:
    """Delete a translator."""
    is_int64(user_id)
    return await self.db.execute("SELECT public.deletetranslator($1)", user_id)
