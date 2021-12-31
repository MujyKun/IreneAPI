from typing import Optional
from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import UserCreds
import json
import aiofiles


class Drive:
    def __init__(self):
        """
        Controls the downloading, listing, and uploading of Google Drive files.
        """
        self.expiry = None
        self.scopes = None
        self.__creds: Optional[UserCreds] = None

    async def create(self):
        """Properly initialize this object."""
        async with aiofiles.open("token.json", "r") as file:
            service_creds = json.loads(await file.read())
            self.scopes = service_creds.pop("scope")
            self.expiry = service_creds.pop("expiry_date")
        self.__creds = UserCreds(scopes=self.scopes, **service_creds)

    async def list_files(self):
        """List the files of a Google Drive account."""
        async with Aiogoogle(user_creds=self.__creds) as aiogoogle:
            drive_v3 = await aiogoogle.discover("drive", "v3")
            json_res = await aiogoogle.as_service_account(
                drive_v3.files.list(),
            )
            for file in json_res["files"]:
                print(file["name"])

    async def download_file(self, file_id, path):
        """Download a google drive file."""
        async with Aiogoogle(user_creds=self.__creds) as aiogoogle:
            drive_v3 = await aiogoogle.discover("drive", "v3")
            await aiogoogle.as_service_account(
                drive_v3.files.get(fileId=file_id, download_file=path, alt="media"),
            )

    async def upload_file(self, path):
        """Upload a file to google drive."""
        async with Aiogoogle(user_creds=self.__creds) as aiogoogle:
            drive_v3 = await aiogoogle.discover("drive", "v3")
            await aiogoogle.as_service_account(drive_v3.files.create(upload_file=path))

    @staticmethod
    def get_id_from_url(url) -> str:
        """Get a file id based on the url."""
        return url.replace("https://drive.google.com/uc?export=view&id=", "")
