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

        async with self._pool.acquire() as connection:
            await connection.execute(query)

    async def fetch_row(self, query: str):
        ...

    async def fetch(self, query: str):
        ...

    async def generate(self):
        ...

    async def _create_pool(self, **login_payload):
        self._pool = await asyncpg.create_pool(command_timeout=60, **login_payload)

