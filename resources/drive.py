from typing import Optional
from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds
import json
import aiofiles


SCOPES = ["https://www.googleapis.com/auth/drive"]


class Drive:
    def __init__(self):
        """
        Controls the downloading, listing, and uploading of Google Drive files.
        """
        self.expiry = None
        self.scopes = None
        self.__service_creds: Optional[ServiceAccountCreds] = None

    async def create(self):
        """Properly initialize this object."""
        async with aiofiles.open("service_account.json", "r") as file:
            service_creds = json.loads(await file.read())
            self.__service_creds = ServiceAccountCreds(**service_creds, scopes=SCOPES)

    async def list_files(self):
        """List the files of a Google Drive account."""
        async with Aiogoogle(service_account_creds=self.__service_creds) as aiogoogle:
            drive_v3 = await aiogoogle.discover("drive", "v3")
            json_res = await aiogoogle.as_user(
                drive_v3.files.list(),
            )
            for file in json_res["files"]:
                print(file["name"])

    async def download_file(self, file_id, path):
        """Download a google drive file."""
        async with Aiogoogle(service_account_creds=self.__service_creds) as aiogoogle:
            drive_v3 = await aiogoogle.discover("drive", "v3")
            requests = drive_v3.files.get(
                fileId=file_id, download_file=path, alt="media"
            )
            results = await aiogoogle.as_service_account(requests)

    async def upload_file(self, path):
        """Upload a file to google drive."""
        async with Aiogoogle(service_account_creds=self.__service_creds) as aiogoogle:
            drive_v3 = await aiogoogle.discover("drive", "v3")
            await aiogoogle.as_user(drive_v3.files.create(upload_file=path))

    @staticmethod
    def get_id_from_url(url) -> str:
        """Get a file id based on the url."""
        return url.replace("https://drive.google.com/uc?export=view&id=", "")
