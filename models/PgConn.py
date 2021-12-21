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

    async def read_sql_file(self, file_name: str):

        ...

    async def execute(self, query: str):
        if not query:
            return

        query = query.replace("\n", "")

        async with self._pool.acquire() as conn:
            await conn.execute(query)

    async def fetch_row(self, query: str, *args, **kwargs):
        if not query:
            return

        async with self._pool.acquire() as conn:
            await conn.fetchrow(query, *args, **kwargs)

    async def fetch(self, query: str, *args, **kwargs):
        if not query:
            return

        async with self._pool.acquire() as conn:
            await conn.fetch(query, *args, **kwargs)

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




        ...

