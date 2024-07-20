from os import listdir, environ
from os.path import isdir, exists
from typing import Optional

import aiofiles
import asyncpg.exceptions
import subprocess


class DbConnection:
    def __init__(
        self, db_host: str, db_name: str, db_user: str, db_pass: str, db_port: int
    ):
        """
        Abstract version for a database connection.

        :param db_host: The database host to connect to.
        :param db_name: Database Name to connect to.
        :param db_user: Database User to log in as.
        :param db_pass: Password of the Database User.
        """
        self._db_host = db_host
        self._db_name = db_name
        self._db_user = db_user
        self._db_port = db_port
        self.__db_pass = db_pass
        self.__db_kwargs = {
            "host": self._db_host,
            "database": self._db_name,
            "user": self._db_user,
            "password": self.__db_pass,
            "port": self._db_port,
        }

    async def connect(self):
        """Connect to the PostgreSQL Database."""

        await self._create_pool(
            **self.__db_kwargs
        )
        await self.update_db_structure(use_terminal=True)
        print(f"Connected to Database {self._db_name} as {self._db_user}.")

    async def execute_sql_file(self, file_path: str, use_terminal=False) -> Optional[str]:
        """Read and execute the queries in a SQL file.

        :param file_path: str
            File name to read and execute.
        :param use_terminal: bool
            Whether to use the terminal for auto executing create files.
        :returns str:
            Code that cannot be executed.
        """
        if use_terminal:
            command = [
                'psql',
                f'--dbname={self._db_name}',
                f'--username={self._db_user}',
                f'--host={self._db_host}',
                f'--port={self._db_port}',
                '--file', file_path
            ]
            env = {'PGPASSWORD': self.__db_pass,
                   **dict(environ)}

            subprocess.run(command, env=env)
            return

        try:
            async with aiofiles.open(file_path, mode="r") as file:
                data = await file.read()
                if "functions" in file_path.lower() or "views" in file_path.lower():
                    return data

                for query in data.split(";"):
                    try:
                        await self.execute(query)
                    except asyncpg.exceptions.UniqueViolationError:
                        print(
                            "Failed to insert metadata as it already exists. "
                            f"If a relation has changed, update it manually. - {query}"
                        )
        except FileNotFoundError:
            print(f"Could not find {file_path} for SQL execution.")
        return ""

    async def execute(self, query: str, *args, **kwargs):
        """Execute a SQL query.

        :param query: (str) SQL Query to execute.
        """

    async def fetch_row(self, query: str, *args, **kwargs):
        """Fetch a row from a SQL query.

        :param query: (str) SQL Query to execute.
        """

    async def fetch(self, query: str, *args, **kwargs):
        """Fetch rows from a SQL query.

        :param query: (str) SQL Query to execute.
        """

    async def _create_pool(self, **login_payload):
        """Create and set the connection pool.

        :param login_payload: The login payload to pass into the concrete class.
        """

    async def update_db_structure(self, use_terminal=True):
        """
        Attempt to create/update the DB structure.

        :param use_terminal: Whether to use the terminal to run the sql scripts
        """
        sql_folder_name = "sql"
        create_file_name = "create.sql"

        folder_names = ["types", "biasgame", "blackjack", "groupmembers", "guessinggame", "interactions", "public",
                        "unscramblegame", "views", "functions", "metadata", "constraints"]

        for folder in folder_names:
            folder_path = f"{sql_folder_name}/{folder}"

            # run the create files in every folder first.
            create_file_path = f"{sql_folder_name}/{folder}/{create_file_name}"
            if exists(create_file_path):
                print(create_file_path)
                await self.execute_sql_file(create_file_path, use_terminal=use_terminal)

            for file in listdir(folder_path):
                if file == create_file_name:
                    continue

                file_path = f"{folder_path}/{file}"
                await self.execute_sql_file(file_path, use_terminal=use_terminal)

    async def get_connection(self):
        """Get a new pool connection.

        This is a connection built manually.
        It must be released/closed using the close_connection method.
        """
        ...

    async def close_connection(self, connection):
        """Releases a connection."""
        ...
