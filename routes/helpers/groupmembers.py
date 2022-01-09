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


@check_permission(permission_level=USER)
async def get_name(requestor: Requestor, name_id: int) -> dict:
    """Get a name's information."""
    is_int64(name_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getnames WHERE nameid = $1", name_id
    )


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


@check_permission(permission_level=USER)
async def get_social(requestor: Requestor, social_id: int) -> dict:
    """Get social information."""
    is_int64(social_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.getsocials WHERE socialid = $1", social_id
    )


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


@check_permission(permission_level=USER)
async def get_positions(requestor: Requestor) -> dict:
    """Get all position information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getpositions")


@check_permission(permission_level=USER)
async def get_fandom(requestor: Requestor, group_id: int) -> dict:
    """Get fandom information."""
    is_int64(group_id)
    return await self.db.fetch_row(
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


@check_permission(permission_level=USER)
async def get_blood_types(requestor: Requestor) -> dict:
    """Get all blood type information."""
    return await self.db.fetch("SELECT * FROM groupmembers.getbloodtypes")
