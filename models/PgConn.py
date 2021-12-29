import asyncpg
from . import DbConnection
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
            return self.records_to_dict(response)

    def records_to_dict(self, records) -> dict:
        """Convert records to a dict."""
        if not records:
            return {"results": None}

        if isinstance(records, asyncpg.Record):
            return {"results": self.record_to_dict(records)}

        final_dict = {"results": {}}
        for count, record in enumerate(records):
            final_dict["results"][count] = self.record_to_dict(record)
        return final_dict

    def record_to_dict(self, record: asyncpg.Record) -> dict:
        """Convert a record to a dict."""
        final_dict = {}
        for key, value in record.items():
            final_dict[key] = value
        return final_dict

    async def fetch(self, query: str, *args, **kwargs) -> dict:
        if not query:
            return {"results": None}

        async with self._pool.acquire() as conn:
            response = await conn.fetch(query, *args, **kwargs)
            return self.records_to_dict(response)

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
