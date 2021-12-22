from . import self, check_permission
from models import Requestor


@check_permission(permission_level=1)
async def ban_user(requestor: Requestor, user_id: int):
    """Add a patron."""
    await self.db.execute(f"SELECT public.botban({user_id})")


@check_permission(permission_level=1)
async def unban_user(requestor: Requestor, user_id: int):
    """Unban a user."""
    await self.db.execute(f"SELECT public.botunban({user_id})")


@check_permission(permission_level=1)
async def add_patron(requestor: Requestor, user_id: int):
    """Add a patron."""
    await self.db.execute(f"SELECT public.addpatron({user_id})")


@check_permission(permission_level=1)
async def add_super_patron(requestor: Requestor, user_id: int):
    """Add a super patron."""
    await self.db.execute(f"SELECT public.addsuperpatron({user_id})")


@check_permission(permission_level=1)
async def add_data_mod(requestor: Requestor, user_id: int):
    """Add a data moderator."""
    await self.db.execute(f"SELECT public.adddatamod({user_id})")


@check_permission(permission_level=1)
async def add_mod(requestor: Requestor, user_id: int):
    """Add a moderator."""
    await self.db.execute(f"SELECT public.addmod({user_id})")


@check_permission(permission_level=1)
async def add_proofreader(requestor: Requestor, user_id: int):
    """Add a proofreader."""
    await self.db.execute(f"SELECT public.addproofreader({user_id})")


@check_permission(permission_level=1)
async def add_translator(requestor: Requestor, user_id: int):
    """Add a translator."""
    await self.db.execute(f"SELECT public.addtranslator({user_id})")


@check_permission(permission_level=1)
async def delete_patron(requestor: Requestor, user_id: int):
    """Delete a patron."""
    await self.db.execute(f"SELECT public.deletepatron({user_id})")


@check_permission(permission_level=1)
async def delete_super_patron(requestor: Requestor, user_id: int):
    """Delete a super patron."""
    await self.db.execute(f"SELECT public.deletesuperpatron({user_id})")


@check_permission(permission_level=1)
async def delete_data_mod(requestor: Requestor, user_id: int):
    """Delete a data moderator."""
    await self.db.execute(f"SELECT public.deletedatamod({user_id})")


@check_permission(permission_level=1)
async def delete_mod(requestor: Requestor, user_id: int):
    """Delete a moderator."""
    await self.db.execute(f"SELECT public.deletemod({user_id})")


@check_permission(permission_level=1)
async def delete_proofreader(requestor: Requestor, user_id: int):
    """Delete a proofreader."""
    await self.db.execute(f"SELECT public.deleteproofreader({user_id})")


@check_permission(permission_level=1)
async def delete_translator(requestor: Requestor, user_id: int):
    """Delete a translator."""
    await self.db.execute(f"SELECT public.deletetranslator({user_id})")