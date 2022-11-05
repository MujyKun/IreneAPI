import asyncio
import datetime
import random
from typing import Optional, List, Dict

import aiogoogle.excs
from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds
import json
import aiofiles
from dataclasses import dataclass

SCOPES = ["https://www.googleapis.com/auth/drive"]


class Google(Aiogoogle):
    """Context manager to auto discover the drive api and add manual open/closing."""
    def __init__(self, creds):
        super(Google, self).__init__(service_account_creds=creds)
        self.drive = None
        self.name = "drive"
        self.version = "v3"

    async def open(self):
        return await self.__aenter__()

    async def close(self):
        return await self.__aexit__(None, None, None)

    async def __aenter__(self):
        session = self._get_session()
        if session is None:
            session = self._set_session()
            await session.__aenter__()
            self.drive = await self.discover(self.name, self.version)
            return self
        raise RuntimeError("Nesting context managers using the same Aiogoogle object is not allowed.")


@dataclass
class QueueItem:
    awaitables: callable
    unique_id = f"{datetime.datetime.now()}-{random.randint(10000, 50000)}"
    done = False
    _results = None
    task = None

    def set_as_done(self):
        self.done = True

    @property
    def results(self):
        return self._results

    def set_results(self, results):
        self._results = results


def exc_handler(loop, context):
    """Change the handler to ignore unclosed connections as
    sessions are spammy even while __aexit__ is being called.
    More Info: https://github.com/aio-libs/aiohttp/issues/5277
    """
    if context["message"] == "Unclosed client session":
        return
    loop.default_exception_handler(context)


class Drive:
    def __init__(self):
        """
        Controls the downloading, listing, and uploading of Google Drive files.
        """
        self.expiry = None
        self.scopes = None
        self.initialized = False
        self.__service_creds: Optional[ServiceAccountCreds] = None
        self.queue = asyncio.Queue()

        # 10 per second is the expected, but the time may be increased if there are ratelimit errors.
        self.seconds_to_accomplish_max_requests = 1
        self.max_requests_per_set_time = 10
        self.google: Optional[Google] = None
        asyncio.get_event_loop().create_task(self._queue_loop())

    def print_queue_size(self):
        print(f"Queue Size: {self.queue.qsize()}")

    async def _queue_loop(self):
        item: QueueItem
        requests_in_time_frame = 0
        while True:
            if not self.initialized:
                await asyncio.sleep(3)

            self.print_queue_size()

            awaitables = []
            items = []
            while not self.queue.empty() and len(awaitables) < self.max_requests_per_set_time:
                item = await self.queue.get()
                awaitables.append(item.awaitables)
                items.append(item)

            requests_in_time_frame += len(items)

            if requests_in_time_frame >= self.max_requests_per_set_time or not awaitables:
                await asyncio.sleep(self.seconds_to_accomplish_max_requests)
                requests_in_time_frame = 0
                if not awaitables:
                    continue

            results = await asyncio.gather(*awaitables)

            for idx, result in enumerate(results, start=0):
                item = items[idx]
                item.set_results(results=result)
                item.set_as_done()

    async def get_results(self, awaitable):
        """Run a request with a queue system to adjust for user rate limits."""
        item = QueueItem(awaitable)
        await self.queue.put(item)
        await self._wait_on_queue_item(item)
        return item.results

    @staticmethod
    async def _wait_on_queue_item(item: QueueItem):
        sleep_time = 0
        while not item.done:
            await asyncio.sleep(sleep_time)
            sleep_time += 0.05

    async def create(self):
        """Properly initialize this object."""
        async with aiofiles.open("service_account.json", "r") as file:
            service_creds = json.loads(await file.read())
            self.__service_creds = ServiceAccountCreds(**service_creds, scopes=SCOPES)
            self.google = Google(creds=self.__service_creds)
            asyncio.get_running_loop().set_exception_handler(exc_handler)
            self.initialized = True

    async def list_files(self):
        """List the files of a Google Drive account."""
        async with self.google as google:
            json_res = await google.as_service_account(google.drive.files.list())
            for file in json_res["files"]:
                print(file["name"])

    async def download_file(self, file_id, path):
        """Download a google drive file."""
        async with self.google as google:
            requests = google.drive.files.get(
                fileId=file_id, download_file=path, alt="media"
            )
            results = await self.get_results((google.as_service_account(requests)))

    async def upload_file(self, path):
        """Upload a file to google drive."""
        async with self.google as google:
            await self.get_results(google.as_service_account(google.drive.files.create(upload_file=path)))

    @staticmethod
    def get_id_from_url(url) -> str:
        """Get a file id based on the url."""
        return url.replace("https://drive.google.com/uc?export=view&id=", "")

    @staticmethod
    def get_folder_id_from_url(url) -> str:
        """Get a folder ID based on the url."""
        return url.replace("https://drive.google.com/drive/folders/", "")

    async def get_nested_files_in_folders(self, folder_id, parent_file=None, faces: Dict[str, int] = None):
        """Process a Google Drive folder ID recursively and concurrently between sub-folders.

        :param folder_id: str
            The drive folder ID to recursively get files for.
        :param parent_file: :ref:`File`
            The parent file if there is one.
        :param faces: Dict[str, int]
            The drive full file path to the number of faces in the media.
            This can be retrieved by calling `convert_os_file_to_faces_dict`
        """
        actual_files = []

        tasks = []

        for file in await self.get_files_in_folder(folder_id, parent_file=parent_file):
            if file.is_folder():
                tasks.append(self.get_nested_files_in_folders(file.id, parent_file=file))
            else:
                actual_files.append(file)

        for file_results in await asyncio.gather(*tasks) or []:
            actual_files += file_results

        if not parent_file and faces:  # This means we are back to our root recursively.
            for file in actual_files:
                file.set_faces(faces=faces.get(file.get_full_path()))

        return actual_files

    async def get_files_in_folder(self, folder_id, parent_file=None):
        """Get all files (including other folders) in a folder. """
        async with self.google as google:
            requests = google.drive.files.list(q=f"'{folder_id}' in parents", pageSize=1000)
            results = await self.get_results(google.as_service_account(requests))
            print(f"Got files for {folder_id}")
        return File.create_many(results.get("files") or [], parent_file=parent_file)


@dataclass
class File:
    """
    Represents a Google Drive file.

    A folder is also considered a file.
    """
    kind: str
    id: str
    name: str
    mimeType: str
    parent_file: Optional[object]  # an optional File
    faces: Optional[int] = None

    def __str__(self):
        return self.name

    def set_faces(self, faces: int):
        """Set the number of faces of the File."""
        self.faces = faces

    def get_full_path(self):
        names = [str(file) for file in self.get_all_parents()]
        names.reverse()
        return '/'.join(names) + f"/{str(self)}"

    @staticmethod
    def create_many(files: List[dict], parent_file):
        return [File(**file, parent_file=parent_file) for file in files]

    def is_folder(self):
        return "vnd.google-apps.folder" in self.mimeType

    def get_root_parent(self):
        """Get the root parent."""
        parent_file = self.parent_file
        while parent_file:
            parent_file = parent_file.parent_file

    def get_all_parents(self):
        parent_file = self.parent_file
        parents = []
        while parent_file:
            parents.append(parent_file)
            parent_file = parent_file.parent_file
        return parents

    def get_parent_with_person_info(self):
        """Get the parent file that contains information about the person or group

        Future folders will be for the affiliation instead.
        """
        parent_file = self.parent_file
        identifiers = ["[", "]", "(", ")"]  # person folders contain stage name and ID
        while parent_file:
            if all(identifier in parent_file.name for identifier in identifiers):
                return parent_file
            parent_file = parent_file.parent_file
        return None

    def get_parent_with_group_info(self):
        """Get the parent file that contains information about the group

        Future folders will be for the affiliation instead.
        """
        parent_file = self.parent_file
        identifiers = ["[", "]"]  # group folders only contain ID.
        most_root_parent_match = None
        while parent_file:
            if all(identifier in parent_file.name for identifier in identifiers):
                most_root_parent_match = parent_file
            parent_file = parent_file.parent_file
        return most_root_parent_match

    def get_link(self):
        """Get the link of the file.

        Accounts for a file being a folder.
        """
        if self.is_folder():
            return f"https://drive.google.com/drive/folders/{self.id}"
        else:
            return f"https://drive.google.com/uc?export=view&id={self.id}"

    def get_file_type_without_dots(self):
        """Get the file type/suffix without any dots."""
        return (self.name.split("."))[-1]


async def convert_os_file_to_faces_dict(full_file_path):
    """
    Convert a log file to a dictionary containing the number of faces for each file.

    A file is expected to be in the format of

    {face count}-{full_file_path}
    an example would be:
    1-TREASURE [181]/Park Jeong Woo (Park Jeongwoo) [817]/Manually Uploaded/1/111.jpg

    That shows the file has one face detected.
    """
    async with aiofiles.open(full_file_path, "r") as file:
        faces_dict = {}
        for line in await file.readlines():
            # Do not split by - as names can consist of a dash.
            # Instead, find the first dash and the rest becomes the file path.
            first_dash = line.find("-")
            if first_dash == -1:
                continue

            face_count = line[:first_dash]
            drive_file_path = line[first_dash + 1:]
            drive_file_path = drive_file_path.replace("\n", "")
            faces_dict[drive_file_path] = int(face_count)
        return faces_dict
