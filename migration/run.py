import os.path
import shutil
from typing import Optional, List

import psycopg2
from dotenv import load_dotenv
from time import perf_counter as clock

"""
Migrate DB Data from IreneV1 to IreneV2

Must have already created the new database.
"""

MIGRATE = False
AVATARS_AND_BANNERS = True  # Whether to move already existing avatars and banners and switch them to the new IDs.
avatar_location = "/var/www/images.irenebot/public_html/avatar"  # set avatar location
banner_location = "/var/www/images.irenebot/public_html/banner"  # set banner location
image_host = "https://images.irenebot.com/"


class BaseEntity:
    def __init__(self):
        self.twitter: Optional[str] = None
        self.youtube: Optional[str] = None
        self.melon: Optional[str] = None
        self.instagram: Optional[str] = None
        self.vlive: Optional[str] = None
        self.spotify: Optional[str] = None
        self.fancafe: Optional[str] = None
        self.facebook: Optional[str] = None
        self.tiktok: Optional[str] = None
        self.thumbnail: Optional[str] = None
        self.banner: Optional[str] = None
        self.tags = None

    def create_social(self):
        n_cursor.execute(
            "SELECT * FROM groupmembers.addsocials(%s, %s, %s, %s, "
            "%s, %s, %s, %s, %s)",
            (
                self.twitter,
                self.youtube,
                self.melon,
                self.instagram,
                self.vlive,
                self.spotify,
                self.fancafe,
                self.facebook,
                self.tiktok,
            ),
        )
        social_id = (n_cursor.fetchone())[0]
        return social_id

    def create_display(self):
        n_cursor.execute(
            "SELECT * FROM groupmembers.adddisplay(%s, %s)",
            (self.thumbnail, self.banner),
        )
        display_id = (n_cursor.fetchone())[0]
        return display_id

    def create_date(self, start, end):
        n_cursor.execute("SELECT * FROM groupmembers.adddate(%s, %s)", (start, end))
        date_id = (n_cursor.fetchone())[0]
        return date_id

    def _create_tag(self):
        tag_ids = []
        if self.tags:
            self.tags = self.tags.replace("\n", "")
            split_tags = self.tags.split(",")
            for tag in split_tags:
                if tag[0] == " ":
                    tag = tag[1::]
                if tag[-1] == " ":
                    tag = tag[:-1]
                n_cursor.execute(
                    "SELECT tagid FROM groupmembers.tag WHERE name = %s", (tag.lower(),)
                )
                tag_result = n_cursor.fetchone()
                if tag_result:
                    tag_id = tag_result[0]
                else:
                    n_cursor.execute(
                        "SELECT * FROM groupmembers.addtag(%s)", (tag.lower(),)
                    )
                    tag_id = n_cursor.fetchone()[0]
                tag_ids.append(tag_id)
        return tag_ids


class Idol(BaseEntity):
    def __init__(self, *args):
        self.new_id = None
        super(Idol, self).__init__()
        (
            self.fullname,
            self.stagename,
            self.old_id,
            self.formerfullname,
            self.formerstagename,
            self.birthdate,
            self.birthcountry,
            self.birthcity,
            self.gender,
            self.description,
            self.height,
            self.twitter,
            self.youtube,
            self.melon,
            self.instagram,
            self.vlive,
            self.spotify,
            self.fancafe,
            self.facebook,
            self.tiktok,
            self.zodiac,
            self.thumbnail,
            self.banner,
            self.bloodtype,
            self.tags,
            self.difficulty,
        ) = args
        self.count = 0

        self.affiliation_ids = []

        self.create_person()

    def create_person(self):
        dateid = self.create_date(self.birthdate, None)
        nameid = self.create_name()
        formernameid = self.create_name(former=True)
        gender = self.gender
        description = self.description
        height = self.height
        displayid = self.create_display()
        socialid = self.create_social()
        locationid = self.create_location()
        bloodid = self.create_blood()
        callcount = self.get_count()

        n_cursor.execute(
            "SELECT * FROM groupmembers.addperson(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                dateid,
                nameid,
                formernameid,
                gender,
                description,
                height,
                displayid,
                socialid,
                locationid,
                bloodid,
                callcount,
            ),
        )
        self.new_id = (n_cursor.fetchone())[0]

        self.create_tags()
        self.create_aliases()

    def create_affiliations(self, groups):
        o_cursor.execute(
            "SELECT groupid FROM groupmembers.idoltogroup WHERE idolid = %s",
            (self.old_id,),
        )
        group_ids = o_cursor.fetchall()
        for group_info in group_ids:
            group_id = group_info[0]
            group = [t_group for t_group in groups if t_group.old_id == group_id]
            if not group:
                continue
            group = group[0]

            if group.old_id == 12:
                # SOLO GROUP --> We now create individual groups for solo idols.
                group = Group(
                    group.old_id,
                    self.stagename,
                    None,
                    None,
                    self.description,
                    self.twitter,
                    self.youtube,
                    self.melon,
                    self.instagram,
                    self.vlive,
                    self.spotify,
                    self.fancafe,
                    self.facebook,
                    self.tiktok,
                    None,
                    None,
                    None,
                    self.thumbnail,
                    self.banner,
                    self.gender,
                    None,
                )

            n_cursor.execute(
                "SELECT groupmembers.addaffiliation(%s, %s, %s, %s)",
                (self.new_id, group.new_id, None, self.stagename),
            )
            aff_info = n_cursor.fetchone()
            aff_id = aff_info[0]
            self.affiliation_ids.append(aff_id)

        if len(self.affiliation_ids) >= 1:
            aff_id = self.affiliation_ids[0]
            o_cursor.execute(
                "SELECT link, groupphoto, facecount, filetype FROM groupmembers.imagelinks WHERE memberid = %s",
                (self.old_id,),
            )
            images = o_cursor.fetchall()
            for link, group_photo, face_count, file_type in images:
                n_cursor.execute(
                    "SELECT groupmembers.addmedia(%s, %s, %s, %s, %s, %s)",
                    (link, face_count, file_type, aff_id, True, False),
                )

    def create_aliases(self):
        o_cursor.execute(
            "SELECT alias FROM groupmembers.aliases WHERE isgroup = 0 AND serverid is NULL AND objectid = %s",
            (self.old_id,),
        )
        aliases = o_cursor.fetchall()

        for alias in aliases:
            n_cursor.execute(
                "SELECT groupmembers.addpersonalias(%s, %s, %s)",
                (alias, self.new_id, None),
            )

    def create_tags(self):
        for tag_id in self._create_tag():
            n_cursor.execute(
                "SELECT * FROM groupmembers.addpersontag(%s, %s)",
                (tag_id, self.new_id),
            )

    def get_count(self):
        if self.count:
            return self.count

        o_cursor.execute(
            "SELECT count FROM groupmembers.count WHERE memberid = %s", (self.old_id,)
        )
        amount = o_cursor.fetchone()
        self.count = 0 if not amount else amount[0]
        return self.count

    def create_name(self, former=False) -> tuple:
        def get_first_and_last(name):
            if not name or "N/A" in name:
                return None, None

            split_name = [t_name for t_name in name.split(" ") if t_name]
            if len(split_name) == 1:
                return None, None

            # majority names are korean; english names will need to be manually adjusted.
            if len(split_name) == 2:
                return split_name[1], split_name[0]
            elif len(split_name) >= 3:
                return "".join(split_name[1 : len(split_name)]), split_name[0]
            else:
                print(f"ERROR: The name {name} could not be properly split.")

        n_cursor.execute(
            "SELECT * FROM groupmembers.addname(%s, %s)",
            get_first_and_last(self.formerfullname if former else self.fullname),
        )
        name_id = (n_cursor.fetchone())[0]
        return name_id

    def create_location(self):
        if self.birthcountry:
            if self.birthcountry.lower() == "china":
                self.birthcountry = "CH"
            self.birthcountry = self.birthcountry.upper()
        else:
            self.birthcountry = None

        if self.birthcity:
            self.birthcity = self.birthcity.title()
        else:
            self.birthcity = None

        n_cursor.execute(
            "SELECT * FROM groupmembers.addlocation(%s, %s)",
            (self.birthcountry, self.birthcity),
        )
        location_id = n_cursor.fetchone()
        return location_id

    def create_blood(self):
        if not self.bloodtype:
            return None

        n_cursor.execute(
            "SELECT bloodid FROM groupmembers.bloodtypes WHERE name = %s",
            (self.bloodtype.upper(),),
        )
        blood_id = n_cursor.fetchone()[0]
        return blood_id


class Group(BaseEntity):
    def __init__(self, *args):
        super(Group, self).__init__()
        (
            self.old_id,
            self.groupname,
            self.debutdate,
            self.disbanddate,
            self.description,
            self.twitter,
            self.youtube,
            self.melon,
            self.instagram,
            self.vlive,
            self.spotify,
            self.fancafe,
            self.facebook,
            self.tiktok,
            self.fandom,
            self.company,
            self.website,
            self.thumbnail,
            self.banner,
            self.gender,
            self.tags,
        ) = args

        self.new_id = None

        self.create_group()

    def create_group(self):
        date_id = self.create_date(self.debutdate, self.disbanddate)
        displayid = self.create_display()
        socialid = self.create_social()
        company_id = self.create_company()

        n_cursor.execute(
            "SELECT * FROM groupmembers.addgroup(%s, %s, %s, %s, %s, %s, %s)",
            (
                self.groupname,
                date_id,
                self.description,
                company_id,
                displayid,
                self.website,
                socialid,
            ),
        )
        self.new_id = (n_cursor.fetchone())[0]
        self.create_tags()
        self.create_aliases()
        self.create_fandom()

    def create_fandom(self):
        if self.fandom:
            n_cursor.execute(
                "SELECT groupmembers.addfandom(%s, %s)", (self.new_id, self.fandom)
            )

    def create_aliases(self):
        o_cursor.execute(
            "SELECT alias FROM groupmembers.aliases WHERE isgroup = 1 AND serverid is NULL AND objectid = %s",
            (self.old_id,),
        )
        aliases = o_cursor.fetchall()

        for alias in aliases:
            n_cursor.execute(
                "SELECT groupmembers.addgroupalias(%s, %s, %s)",
                (alias, self.new_id, None),
            )

    def create_tags(self):
        for tag_id in self._create_tag():
            n_cursor.execute(
                "SELECT * FROM groupmembers.addgrouptag(%s, %s)",
                (tag_id, self.new_id),
            )

    def create_company(self):
        if self.company:
            n_cursor.execute(
                "SELECT companyid FROM groupmembers.company WHERE name = %s",
                (self.company.upper(),),
            )
            company = n_cursor.fetchone()
            if company:
                company_id = company[0]
            else:
                n_cursor.execute(
                    "SELECT groupmembers.addcompany(%s, %s, %s)",
                    (self.company.upper(), None, None),
                )
                company_id = n_cursor.fetchone()[0]
            return company_id


def full_reset():
    """Reset Sequences and Tables"""
    sql_queries = [
        "DELETE FROM groupmembers.name;",
        "DELETE FROM groupmembers.dates;",
        "DELETE FROM groupmembers.socialmedia;",
        "DELETE FROM groupmembers.display;",
        "DELETE FROM groupmembers.location;",
        "DELETE FROM groupmembers.person;",
        "DELETE FROM groupmembers.tag;",
        "DELETE FROM groupmembers.persontags;",
        "DELETE FROM groupmembers.company;",
        "DELETE FROM groupmembers.groups;",
        "DELETE FROM groupmembers.grouptags;",
        "DELETE FROM groupmembers.personaliases;",
        "DELETE FROM groupmembers.groupaliases;",
        "DELETE FROM groupmembers.affiliation;",
        "DELETE FROM groupmembers.media;",
        "DELETE FROM groupmembers.fandom;",
        "DELETE FROM interactions.media;",
        "DELETE FROM interactions.interactiontypes;",
        "ALTER SEQUENCE groupmembers.name_nameid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.dates_dateid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.socialmedia_socialid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.display_displayid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.location_locationid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.person_personid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.tag_tagid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.groups_groupid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.company_companyid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.personaliases_aliasid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.groupaliases_aliasid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.affiliation_affiliationid_seq RESTART;",
        "ALTER SEQUENCE groupmembers.media_mediaid_seq RESTART;",
        "ALTER SEQUENCE interactions.interactiontypes_typeid_seq RESTART;",
    ]
    for sql in sql_queries:
        n_cursor.execute(sql)


def migrate_interactions():
    o_cursor.execute("SELECT url, interaction FROM general.interactions")
    links = o_cursor.fetchall()
    for url, interaction in links:
        n_cursor.execute(
            "SELECT typeid FROM interactions.interactiontypes WHERE name = %s",
            (interaction.lower(),),
        )
        type_info = n_cursor.fetchone()
        if not type_info:
            n_cursor.execute(
                "SELECT interactions.addinteractiontype(%s)", (interaction.lower(),)
            )
            n_cursor.execute(
                "SELECT typeid FROM interactions.interactiontypes WHERE name = %s",
                (interaction.lower(),),
            )
            type_info = n_cursor.fetchone()
        type_id = type_info[0]
        n_cursor.execute(
            "SELECT FROM interactions.addinteractionmedia(%s, %s)", (url, type_id)
        )


def migrate():
    print_time(
        full_reset,
        "Reset Sequences and Tables.",
        "5+ Minutes if Data is fully loaded, otherwise <2 Seconds. ",
    )
    print_time(migrate_interactions, "Add Interactions.", "<2 Seconds")
    idols = print_time(migrate_idols, "Create new Idols/Persons", "<2 Seconds")
    groups = print_time(migrate_groups, "Create new Groups.", "<2 Seconds")
    print_time(create_affs, "Create affiliations and media", "6 Minutes", idols, groups)
    new_db.commit()
    return {"idols": idols, "groups": groups}


def create_affs(idols, groups):
    _ = [idol.create_affiliations(groups) for idol in idols]


def print_time(func, reason, expected_time, *args, **kwargs):
    start = clock()
    print(f"Starting to {reason}. Expected Time: {expected_time}")
    return_val = func(*args, **kwargs)
    total_time = clock() - start
    print(f"{total_time}s to {reason}")
    return return_val


def migrate_idols():
    o_cursor.execute("SELECT * FROM groupmembers.member")
    idols = o_cursor.fetchall()
    return [Idol(*idol) for idol in idols]


def migrate_groups():
    o_cursor.execute("SELECT * FROM groupmembers.groups")
    groups = o_cursor.fetchall()
    return [Group(*group) for group in groups]


def make_avatar_and_banner_folders():
    directories = [
        banner_location + "/person",
        banner_location + "/group",
        avatar_location + "/person",
        avatar_location + "/group",
    ]
    for directory in directories:
        if not os.path.isdir(directory):
            os.mkdir(directory)


def handle_avatars_and_banners(groups=False):
    make_avatar_and_banner_folders()
    if not groups:
        folder_name = "person"
        sql_ = "SELECT p.personid, d.avatar, d.banner, d.displayid FROM groupmembers.person p LEFT JOIN groupmembers.display d ON d.displayid = p.displayid WHERE AVATAR IS NOT NULL OR BANNER IS NOT NULL"
    else:
        folder_name = "group"
        sql_ = "SELECT g.groupid, d.avatar, d.banner, d.displayid FROM groupmembers.groups g LEFT JOIN groupmembers.display d ON d.displayid = g.displayid WHERE AVATAR IS NOT NULL OR BANNER IS NOT NULL"

    n_cursor.execute(sql_)
    display_data = n_cursor.fetchall()
    for object_id, avatar_url, banner_url, display_id in display_data:
        file_name = f"{object_id}.webp"
        if avatar_url:
            original_file_name = get_file_name_from_url(avatar_url)
            avatar_folder_loc = f"{avatar_location}/{folder_name}"
            new_avatar_loc = f"{avatar_folder_loc}/{file_name}"
            avatar_url = f"{image_host}avatar/{folder_name}/{file_name}"
            copy_file(f"{avatar_location}/{original_file_name}", new_avatar_loc)
            n_cursor.execute(
                "UPDATE groupmembers.display SET avatar = %s WHERE displayid = %s",
                (avatar_url, display_id),
            )
        if banner_url:
            original_file_name = get_file_name_from_url(banner_url)
            banner_folder_loc = f"{banner_location}/{folder_name}"
            new_banner_loc = f"{banner_folder_loc}/{file_name}"
            banner_url = f"{image_host}banner/{folder_name}/{file_name}"
            copy_file(f"{banner_location}/{original_file_name}", new_banner_loc)
            n_cursor.execute(
                "UPDATE groupmembers.display SET banner = %s WHERE displayid = %s",
                (banner_url, display_id),
            )
    new_db.commit()


def copy_file(file_location, new_file_path):
    if os.path.isfile(file_location):
        shutil.copy(file_location, new_file_path)


def get_file_name_from_url(url: str):
    if not url:
        return None

    slash_loc = url.rindex("/")
    return url[slash_loc + 1 : :]


def get_id_from_url(url: str):
    if not url:
        return None

    slash_loc = url.rindex("/")
    underscore_loc = url.rindex("_")
    return url[slash_loc + 1 : underscore_loc]


if __name__ == "__main__":
    load_dotenv()
    from os import getenv

    new_postgres_options = {
        "host": getenv("POSTGRES_HOST"),
        "dbname": getenv("POSTGRES_DATABASE"),
        "user": getenv("POSTGRES_USER"),
        "password": getenv("POSTGRES_PASSWORD"),
        "port": getenv("POSTGRES_PORT"),
    }

    old_postgres_options = {
        "host": getenv("POSTGRES_HOST"),
        "dbname": "postgres",
        "user": getenv("POSTGRES_USER"),
        "password": getenv("POSTGRES_PASSWORD"),
        "port": getenv("POSTGRES_PORT"),
    }

    old_db = psycopg2.connect(**old_postgres_options)
    new_db = psycopg2.connect(**new_postgres_options)
    # new_db.autocommit = True
    o_cursor = old_db.cursor()
    n_cursor = new_db.cursor()

    if MIGRATE:
        data = migrate()
    if AVATARS_AND_BANNERS:
        handle_avatars_and_banners()
        handle_avatars_and_banners(groups=True)
