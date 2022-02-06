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


@check_permission(permission_level=SUPER_PATRON)
async def get_person(requestor: Requestor, person_id: int) -> dict:
    """Get a person's information if they exist."""
    is_int64(person_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getpersons WHERE personid = $1", person_id
    )


@check_permission(permission_level=SUPER_PATRON)
async def get_persons(requestor: Requestor) -> dict:
    """Get all person information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getpersons")


@check_permission(permission_level=SUPER_PATRON)
async def get_group(requestor: Requestor, group_id: int) -> dict:
    """Get a group's information if they exist."""
    is_int64(group_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getgroups WHERE groupid = $1", group_id
    )


@check_permission(permission_level=SUPER_PATRON)
async def get_groups(requestor: Requestor) -> dict:
    """Get all group information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getgroups")


@check_permission(permission_level=USER)
async def get_tag(requestor: Requestor, tag_id: int) -> dict:
    """Get a tag's information."""
    is_int64(tag_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.gettags WHERE tagid = $1", tag_id
    )


@check_permission(permission_level=USER)
async def get_tags(requestor: Requestor) -> dict:
    """Get all tag information."""
    return await self.db.fetch("SELECT * FROM groupmembers.gettags")


@check_permission(permission_level=DEVELOPER)
async def add_tag(requestor: Requestor, name) -> dict:
    """Add tag information."""
    return await self.db.fetch_row("SELECT * FROM groupmembers.addtag($1)", name)


@check_permission(permission_level=DEVELOPER)
async def delete_tag(requestor: Requestor, tag_id) -> dict:
    """Delete tag."""
    is_int64(tag_id)
    return await self.db.execute("SELECT * FROM groupmembers.deletetag($1)", tag_id)


@check_permission(permission_level=USER)
async def get_date(requestor: Requestor, date_id: int) -> dict:
    """Get a date's information."""
    is_int64(date_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getdates WHERE dateid = $1", date_id
    )


@check_permission(permission_level=USER)
async def get_dates(requestor: Requestor) -> dict:
    """Get all date information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getdates")


@check_permission(permission_level=DEVELOPER)
async def add_date(requestor: Requestor, start_date, end_date) -> dict:
    """Add date information."""
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.adddate($1, $2)", start_date, end_date
    )


@check_permission(permission_level=DEVELOPER)
async def delete_date(requestor: Requestor, date_id) -> dict:
    """Delete date information."""
    return await self.db.execute("SELECT * FROM groupmembers.deletedate($1)", date_id)


@check_permission(permission_level=USER)
async def get_name(requestor: Requestor, name_id: int) -> dict:
    """Get a name's information."""
    is_int64(name_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getnames WHERE nameid = $1", name_id
    )


@check_permission(permission_level=DEVELOPER)
async def add_name(requestor: Requestor, first_name, last_name) -> dict:
    """Add a name"""
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.addname($1, $2)", first_name, last_name
    )


@check_permission(permission_level=DEVELOPER)
async def delete_name(requestor: Requestor, name_id) -> dict:
    """Delete a name"""
    return await self.db.execute("SELECT * FROM groupmembers.deletename($1)", name_id)


@check_permission(permission_level=USER)
async def get_names(requestor: Requestor) -> dict:
    """Get all name information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getnames")


@check_permission(permission_level=USER)
async def get_company(requestor: Requestor, company_id: int) -> dict:
    """Get a company's information."""
    is_int64(company_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getcompanies WHERE companyid = $1", company_id
    )


@check_permission(permission_level=USER)
async def get_companies(requestor: Requestor) -> dict:
    """Get all company information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getcompanies")


@check_permission(permission_level=DEVELOPER)
async def add_company(requestor: Requestor, name: str, description: str, date_id: int):
    """Add a company."""
    return await self.db.execute(
        "SELECT groupmembers.addcompany($1, $2, $3)", name, description, date_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_company(requestor: Requestor, company_id: int):
    """Delete a company."""
    return await self.db.execute("SELECT groupmembers.deletecompany($1})", company_id)


@check_permission(permission_level=USER)
async def get_display(requestor: Requestor, display_id: int) -> dict:
    """Get a display's information."""
    is_int64(display_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getdisplays WHERE displayid = $1", display_id
    )


@check_permission(permission_level=USER)
async def get_displays(requestor: Requestor) -> dict:
    """Get all display information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getdisplays")


@check_permission(permission_level=DEVELOPER)
async def add_display(requestor: Requestor, avatar: str, banner: str):
    """Add a display."""
    return await self.db.execute(
        "SELECT groupmembers.adddisplay($1, $2)", avatar, banner
    )


@check_permission(permission_level=DEVELOPER)
async def delete_display(requestor: Requestor, display_id: int):
    """Delete a display."""
    return await self.db.execute("SELECT groupmembers.deletedisplay($1})", display_id)


@check_permission(permission_level=USER)
async def get_location(requestor: Requestor, location_id: int) -> dict:
    """Get a location's information."""
    is_int64(location_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getlocations WHERE locationid = $1", location_id
    )


@check_permission(permission_level=USER)
async def get_locations(requestor: Requestor) -> dict:
    """Get all location information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getlocations")


@check_permission(permission_level=DEVELOPER)
async def add_location(requestor: Requestor, country: str, city: str):
    """Add a location."""
    return await self.db.execute(
        "SELECT groupmembers.addlocation($1, $2)", country, city
    )


@check_permission(permission_level=DEVELOPER)
async def delete_location(requestor: Requestor, location_id: int):
    """Delete a location."""
    return await self.db.execute("SELECT groupmembers.deletelocation($1})", location_id)


@check_permission(permission_level=USER)
async def get_media(requestor: Requestor, media_id: int) -> dict:
    """Get media information."""
    is_int64(media_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getmedia WHERE mediaid = $1", media_id
    )


@check_permission(permission_level=USER)
async def get_all_media(requestor: Requestor) -> dict:
    """Get all media information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getmedia")


@check_permission(permission_level=DEVELOPER)
async def add_media(
    requestor: Requestor, link, faces, file_type, affiliation_id, enabled
):
    """Add media."""
    return await self.db.execute(
        "SELECT groupmembers.addmedia($1, $2, $3, $4, $5)",
        link,
        faces,
        file_type,
        affiliation_id,
        enabled,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_media(requestor: Requestor, media_id: int):
    """Delete media."""
    return await self.db.execute("SELECT groupmembers.deletemedia($1})", media_id)


@check_permission(permission_level=USER)
async def get_person_alias(requestor: Requestor, alias_id: int) -> dict:
    """Get person alias information."""
    is_int64(alias_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getpersonaliases WHERE aliasid = $1", alias_id
    )


@check_permission(permission_level=USER)
async def get_person_aliases(requestor: Requestor) -> dict:
    """Get all person alias information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getpersonaliases")


@check_permission(permission_level=DEVELOPER)
async def add_person_alias(
    requestor: Requestor, alias, person_id, guild_id=None
) -> dict:
    """Add a person alias."""
    is_int64(person_id)
    if guild_id:
        is_int64(guild_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.addpersonalias($1, $2, $3)",
        alias,
        person_id,
        guild_id,
    )


@check_permission(permission_level=USER)
async def delete_person_alias(requestor: Requestor, alias_id: int) -> dict:
    """Delete a person alias."""
    return await self.db.execute("SELECT groupmembers.deletepersonalias($1})", alias_id)


@check_permission(permission_level=USER)
async def get_group_alias(requestor: Requestor, alias_id: int) -> dict:
    """Get group alias information."""
    is_int64(alias_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getgroupaliases WHERE aliasid = $1", alias_id
    )


@check_permission(permission_level=USER)
async def get_group_aliases(requestor: Requestor) -> dict:
    """Get all group alias information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getgroupaliases")


@check_permission(permission_level=DEVELOPER)
async def add_group_alias(requestor: Requestor, alias, group_id, guild_id=None) -> dict:
    """Add a group alias."""
    is_int64(group_id)
    if guild_id:
        is_int64(guild_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.addgroupalias($1, $2, $3)",
        alias,
        group_id,
        guild_id,
    )


@check_permission(permission_level=USER)
async def delete_group_alias(requestor: Requestor, alias_id: int) -> dict:
    """Delete a group alias."""
    return await self.db.execute("SELECT groupmembers.deletegroupalias($1})", alias_id)


@check_permission(permission_level=USER)
async def get_social(requestor: Requestor, social_id: int) -> dict:
    """Get social information."""
    is_int64(social_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getsocials WHERE socialid = $1", social_id
    )


@check_permission(permission_level=DEVELOPER)
async def add_social(
    requestor: Requestor,
    twitter,
    youtube,
    melon,
    instagram,
    vlive,
    spotify,
    fancafe,
    facebook,
    tiktok,
) -> dict:
    """Add a social."""
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.addsocials($1, $2, $3, $4, $5, $6, $7, $8, $9)",
        twitter,
        youtube,
        melon,
        instagram,
        vlive,
        spotify,
        fancafe,
        facebook,
        tiktok,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_social(requestor: Requestor, social_id) -> dict:
    """Delete information about social media."""
    is_int64(social_id)
    return await self.db.execute("SELECT FROM groupmembers.deletesocial($1)", social_id)


@check_permission(permission_level=USER)
async def get_socials(requestor: Requestor) -> dict:
    """Get all social information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getsocials")


@check_permission(permission_level=USER)
async def get_position(requestor: Requestor, position_id: int) -> dict:
    """Get position information."""
    is_int64(position_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getpositions WHERE positionid = $1", position_id
    )


@check_permission(permission_level=DEVELOPER)
async def add_position(requestor: Requestor, position_name) -> dict:
    """Add a position"""
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.addposition($1)", position_name
    )


@check_permission(permission_level=DEVELOPER)
async def delete_position(requestor: Requestor, position_id) -> dict:
    """Delete position."""
    is_int64(position_id)
    return await self.db.execute(
        "SELECT FROM groupmembers.deleteposition($1)", position_id
    )


@check_permission(permission_level=USER)
async def get_positions(requestor: Requestor) -> dict:
    """Get all position information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getpositions")


@check_permission(permission_level=DEVELOPER)
async def add_fandom(requestor: Requestor, group_id, fandom_name) -> dict:
    """Add a fandom"""
    return await self.db.execute(
        "SELECT * FROM groupmembers.addfandom($1, $2)", group_id, fandom_name
    )


@check_permission(permission_level=DEVELOPER)
async def delete_fandom(requestor: Requestor, group_id, fandom_name) -> dict:
    """Delete a fandom"""
    return await self.db.execute(
        "SELECT * FROM groupmembers.deletefandom($1, $2)", group_id, fandom_name
    )


@check_permission(permission_level=USER)
async def get_fandoms_by_group(requestor: Requestor, group_id: int) -> dict:
    """Get all fandoms belonging to a group."""
    is_int64(group_id)
    return await self.db.fetch(
        "SELECT * FROM groupmembers.getfandoms WHERE groupid = $1", group_id
    )


@check_permission(permission_level=USER)
async def get_fandoms(requestor: Requestor) -> dict:
    """Get all fandom information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getfandoms")


@check_permission(permission_level=USER)
async def get_affiliation(requestor: Requestor, affiliation_id: int) -> dict:
    """Get affiliation information."""
    is_int64(affiliation_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getaffiliations WHERE affiliationid = $1",
        affiliation_id,
    )


@check_permission(permission_level=DEVELOPER)
async def add_affiliation(
    requestor: Requestor, person_id, group_id, position_ids, stage_name
) -> dict:
    """Add an affiliation"""
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.addaffiliation($1, $2, $3, $4)",
        person_id,
        group_id,
        position_ids,
        stage_name,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_affiliation(requestor: Requestor, affiliation_id) -> dict:
    """Delete an affiliation"""
    return await self.db.execute(
        "SELECT * FROM groupmembers.deleteaffiliation($1)", affiliation_id
    )


@check_permission(permission_level=USER)
async def get_affiliations(requestor: Requestor) -> dict:
    """Get all affiliation information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getaffiliations")


@check_permission(permission_level=USER)
async def get_blood_type(requestor: Requestor, blood_id: int) -> dict:
    """Get blood type information."""
    is_int64(blood_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getbloodtypes WHERE bloodid = $1", blood_id
    )


@check_permission(permission_level=DEVELOPER)
async def add_blood_type(requestor: Requestor, name: str) -> dict:
    """Add a blood type."""
    return await self.db.fetch_row("SELECT * FROM groupmembers.addbloodtype($1)", name)


@check_permission(permission_level=DEVELOPER)
async def delete_blood_type(requestor: Requestor, blood_id: int) -> dict:
    """Delete a blood type."""
    is_int64(blood_id)
    return await self.db.execute(
        "SELECT * FROM groupmembers.deletebloodtype($1)", blood_id
    )


@check_permission(permission_level=USER)
async def get_blood_types(requestor: Requestor) -> dict:
    """Get all blood type information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getbloodtypes")
