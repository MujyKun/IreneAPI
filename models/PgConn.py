import asyncpg
import aiofiles
from . import DbConnection
from os import listdir
from os.path import isdir
from typing import Optional


class PgConnection(DbConnection):
    def __init__(self, *args, **kwargs):
        """
        Concrete version of a database connection using asyncpg.

        :param args: Params for DbConnection
        """
        self._pool: Optional[asyncpg.pool.Pool] = None
        super(PgConnection, self).__init__(*args, **kwargs)

    async def execute(self, query: str, *args, **kwargs):
        query = query.replace("\n", "")

        if not query:
            return {"results": {"success": False, "error": "No Query Found."}}

        async with self._pool.acquire() as conn:
            try:
                await conn.execute(query, *args, **kwargs)
                return {"results": {"success": True}}
            except Exception as e:
                return {"results": {"success": False, "error": f"{e}"}}

    async def fetch_row(self, query: str, *args, **kwargs) -> dict:
        if not query:
            return {"results": None}

        async with self._pool.acquire() as conn:
            response = await conn.fetchrow(query, *args, **kwargs)
            response_as_dict = dict(response)
            return {"results": response_as_dict}

    async def record_to_dict(self):
        """Convert a record to a dict."""

    async def fetch(self, query: str, *args, **kwargs) -> dict:
        if not query:
            return {"results": None}

        async with self._pool.acquire() as conn:
            response = await conn.fetch(query, *args, **kwargs)
            response_as_dict = dict(response)
            return {"results": response_as_dict}

    async def _create_pool(self, **login_payload):
        self._pool = await asyncpg.create_pool(command_timeout=60, **login_payload)

    async def _connect_to_other_database(self, **login_payload):
        self.old_pool = await asyncpg.create_pool(command_timeout=60, **login_payload)

        async with self.old_pool.acquire() as conn:
            # groupmembers
            all_aliases = await conn.fetch("SELECT * FROM groupmembers.aliases")
            data_mods = await conn.fetch("SELECT * FROM groupmembers.datamods")
            groups = await conn.fetch("SELECT * FROM groupmembers.groups")
            idols = await conn.fetch("SELECT * FROM groupmembers.member")
            idol_to_groups = await conn.fetch("SELECT * FROM groupmembers.idoltogroup")
            restricted = await conn.fetch("SELECT * FROM groupmembers.restricted")
            image_links = await conn.fetch("SELECT * FROM groupmembers.imagelinks")
