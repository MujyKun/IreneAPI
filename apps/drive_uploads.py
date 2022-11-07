"""
drive_uploads.py

A Standalone Application
Will extract Google Drive files from folders, associate them with affiliations, and add them to the DB.

Is supportive of both Irene V1 and V2.
"""
import asyncio
import json

import aiofiles

from os import chdir, mkdir, getcwd
from os.path import normpath, dirname, realpath, isdir
from typing import Optional, List

# Set the working directory to the root folder.

app_folder = normpath(dirname(realpath(__file__)))
if app_folder[-1] in ["/", "\\"]:
    app_folder = app_folder[:len(app_folder) - 1]
app_folder = app_folder + r"\.."
chdir(app_folder)
from asyncio import get_event_loop
from resources import drive, File, convert_os_file_to_faces_dict
from models import PgConnection, Requestor
from resources.keys import postgres_options
from time import perf_counter
from datetime import datetime

from routes.helpers import groupmembers, GOD as GOD_ACCESS
GOD = Requestor(-1, GOD_ACCESS)

# A face log file is expected to be in the format of {face count}-{full_file_path}
# an example would be:
# 1-TREASURE [181]/Park Jeong Woo (Park Jeongwoo) [817]/Manually Uploaded/1/111.jpg
# Which shows the file has one face detected and should be a path that Google Drive can recognize.
PATH_TO_FACES = "face_logs.txt"  # Should be in root directory.

# Folder ID present in the Drive URL
# This folder should contain Group folders.
DRIVE_FOLDER_ID = "1GWpFzPtuVOkIfxb9bqSsOLdPiwwnFfNk"

# Irene V1 has a different layout than V2.
# This includes different person and group IDs.
# In addition, V2 has affiliation IDs used instead of person and group IDs.
HANDLE_IRENE_V1 = True

RESULTS_LOCATION_FOLDER = "temp/"
TEMP_FILE_NAME = datetime.now().strftime("%Y%m%d-%H%M%S")
TEMP_FILE_PATH = f"{RESULTS_LOCATION_FOLDER}/{TEMP_FILE_NAME}"

ALLOWED_FILE_TYPES = ["jpg", "png", "jpeg", "jfif", "mp4", "gif", "webm", "webp"]

# A list of folder ids that get searched. Will exclude folder IDs not listed here (aside from the DRIVE_FOLDER_ID)
ONLY_DO = []


async def process_files_to_db():
    """Process the files to be added to the DB."""
    faces = await convert_os_file_to_faces_dict(PATH_TO_FACES) or None
    start = perf_counter()
    affs = (await groupmembers.get_affiliations(GOD))['results']
    groups = (await groupmembers.get_groups(GOD))["results"]
    files = await drive.get_nested_files_in_folders(folder_id=DRIVE_FOLDER_ID, faces=faces,
                                                    only_do=ONLY_DO)

    await log(f"{perf_counter() - start}s to get {len(files)} nested files from folders.")
    tasks = []
    for file in files:
        if HANDLE_IRENE_V1:
            tasks.append(handle_old_layout(file, affs, groups))
        else:
            await handle_new_layout(file)

    results = []
    results += await asyncio.gather(*tasks)
    await add_media_bulk(results)
    await save_results(results)


async def save_results(results: List[tuple]):
    """Save the results to a json file."""
    if not isdir(RESULTS_LOCATION_FOLDER):
        mkdir(RESULTS_LOCATION_FOLDER)

    records = {}
    for record in results:
        if not record:
            continue

        aff_id = record[3]
        if not records.get(aff_id):
            records[aff_id] = 1
        else:
            records[aff_id] += 1

    async with aiofiles.open(f"{TEMP_FILE_PATH}.json", "w") as fp:
        await fp.write(json.dumps(records))


async def log(line: str):
    if not isdir(RESULTS_LOCATION_FOLDER):
        mkdir(RESULTS_LOCATION_FOLDER)

    async with aiofiles.open(f"{TEMP_FILE_PATH}.log", "a") as fp:
        await fp.write(f"{line}\n")


async def handle_old_layout(file: File, affs, groups):
    """Handle the folders in the context of V1 (OLd Group and Idol IDs)"""
    file_type_allowed = True
    group_folder: Optional[File] = file.get_parent_with_group_info()
    person_folder: Optional[File] = file.get_parent_with_person_info()
    args = {}
    if not group_folder or not person_folder:
        await log(f"No Person/Group folder found for {file.get_full_path()}")
        return args
    stage_name = person_folder.name[person_folder.name.index("(") + 1: person_folder.name.rindex(")")].lower()
    group_name = group_folder.name[0: group_folder.name.index("[")].lower()
    group_name_no_spaces = group_name.replace(" ", "")
    for index, values in affs.items():
        aff_id = values["affiliationid"]
        # person_id = values["personid"]
        group_id = values["groupid"]
        aff_stage_name = values["stagename"]

        if stage_name != aff_stage_name.lower():
            continue

        associated_group = None
        for group_index, group_info in groups.items():
            if group_info["groupid"] == group_id or group_info["name"].replace(" ", "").lower() == group_name_no_spaces:
                associated_group = group_info

        if not associated_group:
            continue

        file_type = file.get_file_type_without_dots()
        if file_type not in ALLOWED_FILE_TYPES:
            file_type_allowed = False
            continue

        args = (file.get_link(), file.faces, file_type, aff_id, True, False)
        return args
    if file_type_allowed:
        await log(f"No Affiliation Found for {file.get_full_path()}")
    return args


async def add_media_bulk(args: List[tuple]):
    """Add media in a bulk fashion. Should only be google drive links.

    Susceptible for SQL Injection. Do not use on external links.
    """
    values = [arg for arg in args if arg]
    sql = "INSERT INTO groupmembers.media(link, faces, filetype, affiliationid, enabled, nsfw) " \
          "VALUES ($1, $2, $3, $4, $5, $6) ON CONFLICT DO NOTHING"
    conn = await self.db.get_connection()
    await conn.executemany(sql, values)
    await self.db.close_connection(conn)


async def handle_new_layout(file: File):
    """Handle Irene V2.0's new layout."""

    # extract the affiliation ID from the file's full path and insert the media.
    ...

if __name__ == '__main__':
    loop = get_event_loop()
    try:
        db = PgConnection(**postgres_options)

        # instantiate google drive
        loop.run_until_complete(drive.create())
        drive.print_queue = True

        # update helper usage of the DB.
        from routes import self

        self.db = db

        # connect to db.
        loop.run_until_complete(db.connect())
        loop.run_until_complete(process_files_to_db())

    except KeyboardInterrupt:
        # cancel all tasks lingering
        ...
    except Exception as e:
        print(f"{e}")
