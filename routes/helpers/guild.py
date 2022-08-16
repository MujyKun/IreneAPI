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
from datetime import datetime


@check_permission(permission_level=DEVELOPER)
async def get_prefixes(requestor: Requestor, guild_id: int):
    is_int64(guild_id)
    return await self.db.fetch_row(
        "SELECT * FROM public.getprefixes WHERE guildid = $1", guild_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_all_prefixes(requestor: Requestor):
    return await self.db.fetch("SELECT * FROM public.getprefixes")


@check_permission(permission_level=DEVELOPER)
async def add_prefix(requestor: Requestor, guild_id: int, prefix: str):
    is_int64(guild_id)
    if not prefix:
        return {"results": {"error": "An invalid prefix was entered."}}
    return await self.db.execute("SELECT public.addprefix($1, $2)", guild_id, prefix)


@check_permission(permission_level=DEVELOPER)
async def delete_prefix(requestor: Requestor, guild_id: int, prefix: str):
    is_int64(guild_id)
    return await self.db.execute("SELECT public.deleteprefix($1, $2)", guild_id, prefix)


@check_permission(permission_level=DEVELOPER)
async def add_guild(
    requestor: Requestor,
    guild_id: int,
    name: str,
    emoji_count: int,
    afk_timeout: int,
    icon: str,
    owner_id: int,
    banner: str,
    description: str,
    mfa_level: int,
    splash: str,
    nitro_level: int,
    boosts: int,
    text_channel_count: int,
    voice_channel_count: int,
    category_count: int,
    emoji_limit: int,
    member_count: int,
    role_count: int,
    shard_id: int,
    create_date,
    has_bot: bool,
):
    """Add a guild."""
    try:
        _date = datetime.strptime(
            create_date.replace("+00:00", ""), "%Y-%m-%d %H:%M:%S.%f"
        )
    except Exception as e:
        _date = datetime.strptime(
            create_date.replace("+00:00", ""), "%Y-%m-%d %H:%M:%S"
        )
    return await self.db.execute(
        "SELECT public.addguild($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, "
        "$15, $16, $17, $18, $19, $20, $21)",
        guild_id,
        name,
        emoji_count,
        afk_timeout,
        icon,
        owner_id,
        banner,
        description,
        mfa_level,
        splash,
        nitro_level,
        boosts,
        text_channel_count,
        voice_channel_count,
        category_count,
        emoji_limit,
        member_count,
        role_count,
        shard_id,
        _date,
        has_bot,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_guild(requestor: Requestor, guild_id: int):
    """Delete a guild."""
    return await self.db.execute("SELECT public.deleteguild($1})", guild_id)


@check_permission(permission_level=DEVELOPER)
async def get_guild(requestor: Requestor, guild_id: int):
    """Get a guild."""
    return await self.db.fetch_row(
        "SELECT * FROM public.getguilds WHERE guildid = $1", guild_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_guilds(requestor: Requestor):
    """Get all guilds."""
    return await self.db.fetch("SELECT * FROM public.getguilds")
