import logging

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

        final_dict = {"results": {count: self.record_to_dict(record) for count, record in enumerate(records)}}

        return final_dict

    @staticmethod
    def record_to_dict(record: asyncpg.Record) -> dict:
        """Convert a record to a dict."""
        return dict(record.items())

    async def fetch(self, query: str, *args, **kwargs) -> dict:
        if not query:
            return {"results": None}

        async with self._pool.acquire() as conn:
            response = await conn.fetch(query, *args, **kwargs)
            return self.records_to_dict(response)

    async def _create_pool(self, **login_payload):
        self._pool = await asyncpg.create_pool(
            command_timeout=3600, max_size=500, **login_payload
        )

    async def get_connection(self):
        """Get a new pool connection.

        This is a connection built manually.
        It must be released/closed using the close_connection method.
        """
        return await self._pool.acquire()

    async def close_connection(self, connection):
        """Releases a connection."""
        await self._pool.release(connection)
