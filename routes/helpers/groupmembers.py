import concurrent.futures
from typing import Literal

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
    convert_to_date
)
from models import Requestor
from resources import drive
from resources.keys import person_folder, image_host
from datetime import datetime
from pathlib import Path


DIR_FILE_LIMIT = 1000000
_new_photo_counter = 0


@check_permission(permission_level=DEVELOPER)
async def add_auto_media(
    requestor: Requestor, channel_id: int, affiliation_id: int, hours_after: int
):
    """Add auto media."""
    is_int64(channel_id)
    is_int64(affiliation_id)
    is_int64(hours_after)
    return await self.db.execute(
        "SELECT * FROM groupmembers.addautomedia($1, $2, $3)",
        channel_id,
        affiliation_id,
        hours_after,
    )


@check_permission(permission_level=DEVELOPER)
async def remove_auto_media(requestor: Requestor, channel_id: int, affiliation_id: int):
    """Remove auto media."""
    is_int64(channel_id)
    is_int64(affiliation_id)
    return await self.db.execute(
        "SELECT * FROM groupmembers.deleteautomedia($1, $2)", channel_id, affiliation_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_auto_media(requestor: Requestor):
    """Get all auto media."""
    return await self.db.fetch("SELECT * FROM groupmembers.automedia")


@check_permission(permission_level=SUPER_PATRON)
async def get_person(requestor: Requestor, person_id: int) -> dict:
    """Get a person's information if they exist."""
    is_int64(person_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.persons_full WHERE personid = $1", person_id
    )


@check_permission(permission_level=DEVELOPER)
async def delete_person(requestor: Requestor, person_id: int) -> dict:
    """Delete a group permanently."""
    is_int64(person_id)
    return await self.db.execute(
        "SELECT * FROM groupmembers.deleteperson($1)", person_id
    )


async def _get_media_info(object_id: int, object_id_type: Literal['person', 'affiliation', 'group', 'media'] = "person") -> dict:
    """
    Get the media information for a person, group, or affiliation.

    WARNING: An internal function that should not be accessed directly by a user since object_id_type is implemented
    with string manipulation and can be subject to SQL Injection.

    NOTE: object_id_type can also support the input of "media", but is suited for "person", "affiliation", or "group".
    """
    is_int64(object_id)
    assert object_id_type in ['person', 'affiliation', 'group', 'media'], f"Unknown Media Type - {object_id_type}"
    return await self.db.fetch(
        f"SELECT * FROM groupmembers.media_full WHERE {object_id_type}id = $1", object_id
    )


@check_permission(permission_level=SUPER_PATRON)
async def get_person_media_info(requestor: Requestor, person_id: int) -> dict:
    """Get a person's media information."""
    return await _get_media_info(person_id, "person")


@check_permission(permission_level=SUPER_PATRON)
async def get_group_media_info(requestor: Requestor, group_id: int) -> dict:
    """Get a group's media information."""
    return await _get_media_info(group_id, "group")


@check_permission(permission_level=SUPER_PATRON)
async def get_affiliation_media_info(requestor: Requestor, affiliation_id: int) -> dict:
    """Get an affiliation's media information."""
    return await _get_media_info(affiliation_id, "affiliation")


async def _generate_media(
    object_id: int,
    min_faces: int = 1,
    max_faces: int = 999,
    file_type=None,
    nsfw=True,
    enabled=True,
    object_id_type="person",
):
    """
    Generate and download the media for a person, group, or affiliation based on set filters.

    WARNING: An internal function that should not be accessed directly by a user since object_id_type is implemented
    with string manipulation and can be subject to SQL Injection.

    NOTE: object_id_type can also support the input of "media", but is suited for "person", "affiliation", or "group".
    as a specific media id cannot be filtered.
    """
    is_int64(object_id)
    is_int64(min_faces)
    is_int64(max_faces)

    args: tuple = (object_id, min_faces, max_faces, nsfw, enabled)
    query = (
        f"SELECT * FROM groupmembers.media_full WHERE {object_id_type}id = $1 AND faces > $2 AND faces < $3 "
        "AND nsfw = $4 AND enabled = $5"
    )
    if file_type:
        args = args.__add__((file_type,))
        query += " AND filetype = $6"
    query += "ORDER BY RANDOM() LIMIT 1"
    media_info = await self.db.fetch_row(query, *args)
    return await download_and_get_image_host_url(media_info)


@check_permission(permission_level=SUPER_PATRON)
async def get_image_host_url(requestor: Requestor, media_id: int):
    is_int64(media_id)
    media_info = await self.db.fetch_row(
        "SELECT * FROM groupmembers.media_full WHERE mediaid = $1", media_id
    )
    return await download_and_get_image_host_url(media_info)


def blocking_remove_oldest_files():
    """Remove the oldest files in the person directory if it surpasses the file limit."""
    from os import listdir, unlink
    from os.path import getctime

    files = listdir(person_folder)
    if len(files) < DIR_FILE_LIMIT:
        return

    webp_files = [
        f"{person_folder}{file_name}"
        for file_name in files
        if file_name.endswith(".webp")
    ]
    sorted_by_oldest_files = sorted(webp_files, key=getctime)
    _ = [
        unlink(file_path)
        for file_path in sorted_by_oldest_files[0 : DIR_FILE_LIMIT // 2]
    ]


async def download_and_get_image_host_url(media_info):
    """
    Download and get the image host's URL.
    """
    results = media_info.get("results", {})
    if not results:
        return media_info

    media_id = results.get("mediaid")
    file_type = results.get("filetype")

    if not media_id or not file_type:
        return media_info

    file_path = determine_file_path(person_folder, media_id, file_type)
    g_drive_id = drive.get_id_from_url(results.get("link"))

    await drive.download_file(g_drive_id, file_path)
    await drive.convert_to_webp(file_path, file_path)

    # Set the host URL based on file type
    media_info["results"]["host"] = generate_host_url(image_host, media_id, file_type)

    # Check file limit and remove oldest files if necessary
    global _new_photo_counter
    if _new_photo_counter > DIR_FILE_LIMIT * 0.5:
        _new_photo_counter = 0
        with concurrent.futures.ThreadPoolExecutor() as pool:
            future = pool.submit(blocking_remove_oldest_files)

    _new_photo_counter += 1
    return media_info


def determine_file_path(folder, media_id, file_type):
    """
    Determine the file path based on media information.
    """
    file_extension = ".webp" if file_type in ["jpeg", "png", "jpg", "jfif", "webp"] else f".{file_type}"
    return str(Path(folder) / f"{media_id}{file_extension}")


def generate_host_url(base_url, media_id, file_type):
    """
    Generate the host URL based on media information.
    """
    if file_type == "gif":
        return f"{base_url}idol/{media_id}.gif"
    return f"{base_url}{media_id}"


@check_permission(permission_level=SUPER_PATRON)
async def generate_media_person(
    requestor: Requestor,
    person_id: int,
    min_faces: int = 1,
    max_faces: int = 999,
    file_type=None,
    nsfw=True,
    enabled=True,
) -> dict:
    """Generate media for a person."""
    return await _generate_media(
        person_id,
        min_faces,
        max_faces,
        file_type,
        nsfw,
        enabled,
        object_id_type="person",
    )


@check_permission(permission_level=SUPER_PATRON)
async def generate_media_group(
    requestor: Requestor,
    group_id: int,
    min_faces: int = 1,
    max_faces: int = 999,
    file_type=None,
    nsfw=True,
    enabled=True,
) -> dict:
    """Generate media for a group."""
    return await _generate_media(
        group_id,
        min_faces,
        max_faces,
        file_type,
        nsfw,
        enabled,
        object_id_type="group",
    )


@check_permission(permission_level=SUPER_PATRON)
async def generate_media_affiliation(
    requestor: Requestor,
    affiliation_id: int,
    min_faces: int = 1,
    max_faces: int = 999,
    file_type=None,
    nsfw=True,
    enabled=True,
) -> dict:
    """Generate media for an affiliation."""
    return await _generate_media(
        affiliation_id,
        min_faces,
        max_faces,
        file_type,
        nsfw,
        enabled,
        object_id_type="affiliation",
    )


@check_permission(permission_level=SUPER_PATRON)
async def get_persons(requestor: Requestor) -> dict:
    """Get all person information."""
    return await self.db.fetch("SELECT * FROM groupmembers.persons_full")


@check_permission(permission_level=SUPER_PATRON)
async def get_group(requestor: Requestor, group_id: int) -> dict:
    """Get a group's information if they exist."""
    is_int64(group_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.groups_full WHERE groupid = $1", group_id
    )


@check_permission(permission_level=DEVELOPER)
async def add_group(
    requestor: Requestor,
    group_name,
    description,
    company_id,
    display_id,
    website,
    social_id,
    tag_ids,
    debut_date,
    disband_date
) -> dict:
    """Add a group."""

    results = await self.db.fetch_row(
        "SELECT * FROM groupmembers.addgroup($1, $2, $3, $4, $5, $6, $7, $8, $9)",
        group_name,
        description,
        company_id,
        display_id,
        website,
        social_id,
        tag_ids,
        convert_to_date(debut_date),
        convert_to_date(disband_date)
    )
    if results:
        t_results = results.get("results")
        if t_results:
            group_id = t_results["t_group_id"]
            for tag_id in tag_ids:
                await add_group_tag(requestor, tag_id, group_id)
    return results


@check_permission(permission_level=DEVELOPER)
async def add_person(
    requestor: Requestor,
    name_id,
    former_name_id,
    gender,
    description,
    height,
    display_id,
    social_id,
    location_id,
    tag_ids,
    blood_type,
    call_count,
    birth_date,
    death_date,
) -> dict:
    """Add a person."""
    results = await self.db.fetch_row(
        "SELECT * FROM groupmembers.addperson($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)",
        name_id,
        former_name_id,
        gender,
        description,
        height,
        display_id,
        social_id,
        location_id,
        blood_type,
        call_count,
        convert_to_date(birth_date),
        convert_to_date(death_date),
    )
    if results:
        t_results = results.get("results")
        if t_results:
            person_id = t_results["t_person_id"]
            for tag_id in tag_ids:
                await add_person_tag(requestor, tag_id, person_id)
    return results


@check_permission(permission_level=DEVELOPER)
async def add_person_tag(requestor: Requestor, tag_id, person_id):
    return await self.db.execute(
        "SELECT * FROM groupmembers.addpersontag($1, $2)", tag_id, person_id
    )


@check_permission(permission_level=DEVELOPER)
async def add_group_tag(requestor: Requestor, tag_id, group_id):
    return await self.db.execute(
        "SELECT * FROM groupmembers.addgrouptag($1, $2)", tag_id, group_id
    )


@check_permission(permission_level=SUPER_PATRON)
async def get_groups(requestor: Requestor) -> dict:
    """Get all group information."""
    return await self.db.fetch("SELECT * FROM groupmembers.groups_full")


@check_permission(permission_level=DEVELOPER)
async def delete_group(requestor: Requestor, group_id: int) -> dict:
    """Delete a group permanently."""
    is_int64(group_id)
    return await self.db.execute("SELECT * FROM groupmembers.deletegroup($1)", group_id)


@check_permission(permission_level=USER)
async def get_tag(requestor: Requestor, tag_id: int) -> dict:
    """Get a tag's information."""
    is_int64(tag_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.tags WHERE tagid = $1", tag_id
    )


@check_permission(permission_level=USER)
async def get_tags(requestor: Requestor) -> dict:
    """Get all tag information."""
    return await self.db.fetch("SELECT * FROM groupmembers.tags")


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
async def get_name(requestor: Requestor, name_id: int) -> dict:
    """Get a name's information."""
    is_int64(name_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.names WHERE nameid = $1", name_id
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
    return await self.db.fetch("SELECT * FROM groupmembers.names")


@check_permission(permission_level=USER)
async def get_company(requestor: Requestor, company_id: int) -> dict:
    """Get a company's information."""
    is_int64(company_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.companies WHERE companyid = $1", company_id
    )


@check_permission(permission_level=USER)
async def get_companies(requestor: Requestor) -> dict:
    """Get all company information."""
    return await self.db.fetch("SELECT * FROM groupmembers.companies")


@check_permission(permission_level=DEVELOPER)
async def add_company(requestor: Requestor, name: str, description: str, start_date: str, end_date: str):
    """Add a company."""
    return await self.db.execute(
        "SELECT groupmembers.addcompany($1, $2, $3, $4)", name, description, convert_to_date(start_date),
        convert_to_date(end_date)
    )


@check_permission(permission_level=DEVELOPER)
async def delete_company(requestor: Requestor, company_id: int):
    """Delete a company."""
    return await self.db.execute("SELECT groupmembers.deletecompany($1)", company_id)


@check_permission(permission_level=USER)
async def get_display(requestor: Requestor, display_id: int) -> dict:
    """Get a display's information."""
    is_int64(display_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.displays WHERE displayid = $1", display_id
    )


@check_permission(permission_level=USER)
async def get_displays(requestor: Requestor) -> dict:
    """Get all display information."""
    return await self.db.fetch("SELECT * FROM groupmembers.displays")


@check_permission(permission_level=DEVELOPER)
async def add_display(requestor: Requestor, avatar: str, banner: str):
    """Add a display."""
    return await self.db.execute(
        "SELECT groupmembers.adddisplay($1, $2)", avatar, banner
    )


@check_permission(permission_level=DEVELOPER)
async def delete_display(requestor: Requestor, display_id: int):
    """Delete a display."""
    return await self.db.execute("SELECT groupmembers.deletedisplay($1)", display_id)


@check_permission(permission_level=USER)
async def get_location(requestor: Requestor, location_id: int) -> dict:
    """Get a location's information."""
    is_int64(location_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.locations WHERE locationid = $1", location_id
    )


@check_permission(permission_level=USER)
async def get_locations(requestor: Requestor) -> dict:
    """Get all location information."""
    return await self.db.fetch("SELECT * FROM groupmembers.locations")


@check_permission(permission_level=DEVELOPER)
async def add_location(requestor: Requestor, country: str, city: str):
    """Add a location."""
    return await self.db.execute(
        "SELECT groupmembers.addlocation($1, $2)", country, city
    )


@check_permission(permission_level=DEVELOPER)
async def delete_location(requestor: Requestor, location_id: int):
    """Delete a location."""
    return await self.db.execute("SELECT groupmembers.deletelocation($1)", location_id)


@check_permission(permission_level=DEVELOPER)
async def get_media(requestor: Requestor, media_id: int) -> dict:
    """Get media information."""
    is_int64(media_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.media_full WHERE mediaid = $1", media_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_all_media(requestor: Requestor) -> dict:
    """Get all media information."""
    return await self.db.fetch("SELECT * FROM groupmembers.media_full")


@check_permission(permission_level=DEVELOPER)
async def get_media_by_affiliations(
    requestor: Requestor, affiliation_ids, limit=None, count_only=False
):
    """Get all medias that belong to certain affiliations."""
    return_val = "mediaid"
    if count_only:
        return_val = f"COUNT({return_val})"

    return await self.db.fetch(
        f"SELECT {return_val} FROM groupmembers.media_full WHERE affiliationid = any($1) ORDER BY RANDOM() LIMIT $2",
        affiliation_ids,
        limit,
    )


@check_permission(permission_level=DEVELOPER)
async def upsert_media_difficulty(
    requestor: Requestor, media_id, failed_guesses, correct_guesses
):
    """Upsert media difficulty."""
    return await self.db.execute(
        "SELECT * FROM guessinggame.upsertmediadifficulty($1, $2, $3)",
        media_id,
        failed_guesses,
        correct_guesses,
    )


@check_permission(permission_level=DEVELOPER)
async def add_media(
    requestor: Requestor, link, faces, file_type, affiliation_id, enabled, is_nsfw
):
    """Add media."""
    return await self.db.execute(
        "SELECT groupmembers.addmedia($1, $2, $3, $4, $5, $6)",
        link,
        faces,
        file_type,
        affiliation_id,
        enabled,
        is_nsfw,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_media(requestor: Requestor, media_id: int):
    """Delete media."""
    return await self.db.execute("SELECT groupmembers.deletemedia($1)", media_id)


@check_permission(permission_level=USER)
async def get_person_alias(requestor: Requestor, alias_id: int) -> dict:
    """Get person alias information."""
    is_int64(alias_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.personaliases WHERE aliasid = $1", alias_id
    )


@check_permission(permission_level=USER)
async def get_person_aliases(requestor: Requestor) -> dict:
    """Get all person alias information."""
    return await self.db.fetch("SELECT * FROM groupmembers.personaliases")


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
    return await self.db.execute("SELECT groupmembers.deletepersonalias($1)", alias_id)


@check_permission(permission_level=USER)
async def get_group_alias(requestor: Requestor, alias_id: int) -> dict:
    """Get group alias information."""
    is_int64(alias_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.groupaliases WHERE aliasid = $1", alias_id
    )


@check_permission(permission_level=USER)
async def get_group_aliases(requestor: Requestor) -> dict:
    """Get all group alias information."""
    return await self.db.fetch("SELECT * FROM groupmembers.groupaliases")


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
    return await self.db.execute("SELECT groupmembers.deletegroupalias($1)", alias_id)


@check_permission(permission_level=USER)
async def get_social(requestor: Requestor, social_id: int) -> dict:
    """Get social information."""
    is_int64(social_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.socialmedia WHERE socialid = $1", social_id
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
    return await self.db.fetch("SELECT * FROM groupmembers.socialmedia")


@check_permission(permission_level=USER)
async def get_position(requestor: Requestor, position_id: int) -> dict:
    """Get position information."""
    is_int64(position_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.positions WHERE positionid = $1", position_id
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
    return await self.db.fetch("SELECT * FROM groupmembers.positions")


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
        "SELECT * FROM groupmembers.fandoms WHERE groupid = $1", group_id
    )


@check_permission(permission_level=USER)
async def get_fandoms(requestor: Requestor) -> dict:
    """Get all fandom information."""
    return await self.db.fetch("SELECT * FROM groupmembers.fandoms")


@check_permission(permission_level=USER)
async def get_affiliation(requestor: Requestor, affiliation_id: int) -> dict:
    """Get affiliation information."""
    is_int64(affiliation_id)
    return await self.db.fetch_row(
        "SELECT * FROM groupmembers.affiliations WHERE affiliationid = $1",
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
    return await self.db.fetch("SELECT * FROM groupmembers.affiliations")


def get_media_kwargs(requestor, user_args):
    """Get media kwargs based on user args."""
    kwargs = {"requestor": requestor}
    min_faces = user_args.get("min_faces")
    max_faces = user_args.get("max_faces")
    file_type = user_args.get("file_type")
    nsfw = user_args.get("nsfw")
    enabled = user_args.get("enabled")
    if min_faces is not None:
        kwargs["min_faces"] = min_faces
    if max_faces is not None:
        kwargs["max_faces"] = max_faces
    if file_type is not None:
        kwargs["file_type"] = file_type
    if nsfw is not None:
        kwargs["nsfw"] = nsfw
    if enabled is not None:
        kwargs["enabled"] = enabled
    return kwargs
