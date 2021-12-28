from . import self, check_permission
from models import Requestor


@check_permission(permission_level=1)
async def get_user(requestor: Requestor, user_id: int) -> dict:
    """Get a user's information if they exist."""
    return await self.db.fetch_row("SELECT public.getuser($1)", user_id)


@check_permission(permission_level=1)
async def add_user(requestor: Requestor, user_id: int) -> dict:
    """Add a user."""
    return await self.db.fetch_row("SELECT public.adduser($1)", user_id)


@check_permission(permission_level=1)
async def delete_user(requestor: Requestor, user_id: int) -> dict:
    """Delete a user."""
    return await self.db.fetch_row("SELECT public.deleteuser($1)", user_id)


@check_permission(permission_level=1)
async def get_user_banned(requestor: Requestor, user_id: int) -> dict:
    """Check if a user is banned."""
    return await self.db.fetch_row("SELECT public.getbotban($1)", user_id)


@check_permission(permission_level=1)
async def ban_user(requestor: Requestor, user_id: int) -> dict:
    """Ban a user."""
    return await self.db.execute("SELECT public.botban($1)", user_id)


@check_permission(permission_level=1)
async def unban_user(requestor: Requestor, user_id: int) -> dict:
    """Unban a user."""
    return await self.db.execute("SELECT public.botunban($1)", user_id)


@check_permission(permission_level=1)
async def add_patron(requestor: Requestor, user_id: int) -> dict:
    """Add a patron."""
    return await self.db.execute("SELECT public.addpatron($1)", user_id)


@check_permission(permission_level=1)
async def get_user_patron(requestor: Requestor, user_id: int) -> dict:
    """Check if the user is a patron."""
    return await self.db.fetch_row("SELECT public.getpatronstatus($1)", user_id)


@check_permission(permission_level=1)
async def add_super_patron(requestor: Requestor, user_id: int) -> dict:
    """Add a super patron."""
    return await self.db.execute("SELECT public.addsuperpatron($1)", user_id)


@check_permission(permission_level=1)
async def add_data_mod(requestor: Requestor, user_id: int) -> dict:
    """Add a data moderator."""
    return await self.db.execute("SELECT public.adddatamod($1)", user_id)


@check_permission(permission_level=1)
async def add_mod(requestor: Requestor, user_id: int) -> dict:
    """Add a moderator."""
    return await self.db.execute("SELECT public.addmod($1)", user_id)


@check_permission(permission_level=1)
async def add_proofreader(requestor: Requestor, user_id: int) -> dict:
    """Add a proofreader."""
    return await self.db.execute("SELECT public.addproofreader($1)", user_id)


@check_permission(permission_level=1)
async def add_translator(requestor: Requestor, user_id: int) -> dict:
    """Add a translator."""
    return await self.db.execute("SELECT public.addtranslator($1)", user_id)


@check_permission(permission_level=1)
async def delete_patron(requestor: Requestor, user_id: int) -> dict:
    """Delete a patron."""
    return await self.db.execute("SELECT public.deletepatron($1)", user_id)


@check_permission(permission_level=1)
async def delete_super_patron(requestor: Requestor, user_id: int) -> dict:
    """Delete a super patron."""
    return await self.db.execute("SELECT public.deletesuperpatron($1)", user_id)


@check_permission(permission_level=1)
async def delete_data_mod(requestor: Requestor, user_id: int) -> dict:
    """Delete a data moderator."""
    return await self.db.execute("SELECT public.deletedatamod($1)", user_id)


@check_permission(permission_level=1)
async def delete_mod(requestor: Requestor, user_id: int) -> dict:
    """Delete a moderator."""
    return await self.db.execute("SELECT public.deletemod($1)", user_id)


@check_permission(permission_level=1)
async def delete_proofreader(requestor: Requestor, user_id: int) -> dict:
    """Delete a proofreader."""
    return await self.db.execute("SELECT public.deleteproofreader($1)", user_id)


@check_permission(permission_level=1)
async def delete_translator(requestor: Requestor, user_id: int) -> dict:
    """Delete a translator."""
    return await self.db.execute("SELECT public.deletetranslator($1)", user_id)
