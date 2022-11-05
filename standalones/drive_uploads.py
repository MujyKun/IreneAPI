"""
drive_uploads.py

A Standalone Application
Will extract Google Drive files from folders, associate them with affiliations, and add them to the DB.

Is supportive of both Irene V1 and V2.
"""
import json
import os

import aiofiles

from os import chdir
from os.path import normpath, dirname, realpath, isdir
from typing import Optional

# Set the working directory to the root folder.
chdir(normpath(dirname(realpath(__file__))) + r'\..')
from asyncio import get_event_loop
from resources import drive, File, convert_os_file_to_faces_dict
from models import PgConnection, Requestor
from resources.keys import postgres_options
from time import perf_counter

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


async def process_files_to_db():
    """Process the files to be added to the DB."""
    faces = await convert_os_file_to_faces_dict(PATH_TO_FACES) or None
    start = perf_counter()
    files = await drive.get_nested_files_in_folders(folder_id=DRIVE_FOLDER_ID, faces=faces)
    affs = (await groupmembers.get_affiliations(GOD))['results']
    print(f"{perf_counter() - start} to get {len(files)} nested files from folders.")
    successes = dict()
    for file in files:
        if HANDLE_IRENE_V1:
            aff_id, success = await handle_old_layout(file, affs)
            if success:
                amount_of_successes = successes.get(aff_id) or 0
                successes[aff_id] = amount_of_successes + 1
        else:
            await handle_new_layout(file)
    await save_results(successes)


async def save_results(results: dict):
    """Save the results to a json file."""
    from datetime import datetime

    if not isdir(RESULTS_LOCATION_FOLDER):
        os.mkdir(RESULTS_LOCATION_FOLDER)

    file_name = datetime.now().strftime("%Y%m%d-%H%M%S") + ".json"
    async with aiofiles.open(f"{RESULTS_LOCATION_FOLDER}/{file_name}", "w") as fp:
        await fp.write(json.dumps(results))


async def handle_old_layout(file: File, affs):
    """Handle the folders in the context of V1 (OLd Group and Idol IDs)"""
    group_folder: Optional[File] = file.get_parent_with_group_info()
    person_folder: Optional[File] = file.get_parent_with_person_info()
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

        group_info = (await groupmembers.get_group(GOD, group_id=group_id))["results"]
        if group_info["name"].replace(" ", "").lower() != group_name_no_spaces:
            continue

        # we can now add the media to the affiliation.
        results = await groupmembers.add_media(GOD, link=file.get_link(), faces=file.faces,
                                               file_type=file.get_file_type_without_dots(),
                                               affiliation_id=aff_id, enabled=True, is_nsfw=False)
        return aff_id, results["results"]["success"]  # False if there is a duplicate.
    print(f"No Affiliation Found for {file.get_full_path()}")
    return 0, False


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
