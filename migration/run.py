import psycopg2
from dotenv import load_dotenv

"""
Migrate DB Data from IreneV1 to IreneV2
"""


class Idol:
    def __init__(self, *args):
        self.new_id = None
        self.fullname = args[0]
        self.stagename = args[1]
        self.old_id = args[2]
        self.formerfullname = args[3]
        self.formerstagename = args[4]
        self.birthdate = args[5]
        self.birthcountry = args[6]
        self.birthcity = args[7]
        self.gender = args[8]
        self.description = args[9]
        self.height = args[10]
        self.twitter = args[11]
        self.youtube = args[12]
        self.melon = args[13]
        self.instagram = args[14]
        self.vlive = args[15]
        self.spotify = args[16]
        self.fancafe = args[17]
        self.facebook = args[18]
        self.tiktok = args[19]
        self.zodiac = args[20]
        self.thumbnail = args[21]
        self.banner = args[22]
        self.bloodtype = args[23]
        self.tags = args[24]
        self.difficulty = args[25]
        self.count = 0

        self.create_person()

    def create_person(self):
        personid = ...
        dateid = self.create_date()
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

        new_db.commit()

    def create_tags(self):
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

    def create_display(self):
        n_cursor.execute(
            "SELECT * FROM groupmembers.adddisplay(%s, %s)",
            (self.thumbnail, self.banner),
        )
        display_id = (n_cursor.fetchone())[0]
        return display_id

    def create_date(self):
        n_cursor.execute(
            "SELECT * FROM groupmembers.adddate(%s, %s)", (self.birthdate, None)
        )
        date_id = (n_cursor.fetchone())[0]
        return date_id

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


def migrate_idols():
    o_cursor.execute("SELECT * FROM groupmembers.member")
    idols = o_cursor.fetchall()
    idol_objs = [Idol(*idol) for idol in idols]


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

    migrate_idols()
