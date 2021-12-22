from os import listdir
from os.path import isdir
import aiofiles
import asyncio
from . import hash_token

import asyncpg.exceptions


class DbConnection:
    def __init__(self, db_host: str, db_name: str, db_user: str, db_pass: str, db_port: int):
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

    async def connect(self):
        """Connect to the PostgreSQL Database."""

        await self._create_pool(**{
            "host": self._db_host,
            "database": self._db_name,
            "user": self._db_user,
            "password": self.__db_pass,
            "port": self._db_port
        })
        await self.update_db_structure()
        print(f"Connected to Database {self._db_name} as {self._db_user}.")
        # await self.add_token(169401247374376960, hash_token("Bearer test"), 1)
        # print("Added Token.")
        # await self.migration()

    async def add_token(self, user_id: int, unhashed_token: str, access_id: int):
        ...

    async def get_token(self, user_id):
        ...

    async def get_permission_level(self, user_id: int):
        ...

    async def execute_sql_file(self, file_name: str) -> str:
        """Read and execute the queries in a SQL file.

        :param file_name: str File name to read and execute.
        :returns str: Code that cannot be executed.
        """
        try:

            async with aiofiles.open(file_name, mode='r') as file:
                data = await file.read()
                if "functions" in file_name.lower():
                    return data

                for query in data.split(";"):
                    try:
                        await self.execute(query)
                    except asyncpg.exceptions.UniqueViolationError:
                        print("Failed to insert metadata as it already exists. "
                              f"If a relation has changed, update it manually. - {query}")
        except FileNotFoundError:
            print(f"Could not find {file_name} for SQL execution.")
        return ""

    async def execute(self, query: str):
        """Execute a SQL query.

        :param query: (str) SQL Query to execute.
        """

    async def fetch_row(self, query: str):
        """Fetch a row from a SQL query.

        :param query: (str) SQL Query to execute.
        """

    async def fetch(self, query: str):
        """Fetch rows from a SQL query.

        :param query: (str) SQL Query to execute.
        """

    async def _create_pool(self, **login_payload):
        """Create and set the connection pool.

        :param login_payload: The login payload to pass into the concrete class.
        """

    async def update_db_structure(self):
        """Attempt to create the DB structure."""
        sql_folder_name = "sql"
        create_file_name = "create.sql"
        inexecutable_queries = ""
        execute_later = ["metadata", "constraints", "views"]
        for file in listdir(sql_folder_name):
            if file in execute_later:
                # process metadata at the end
                continue

            if isdir(f"{sql_folder_name}/{file}"):
                # run the create files first.
                if file != "functions":
                    create_file = f"{sql_folder_name}/{file}/{create_file_name}"
                    inexecutable_queries += await self.execute_sql_file(create_file)

                for t_file in listdir(f"{sql_folder_name}/{file}"):
                    if t_file != create_file_name:
                        inexecutable_queries += await self.execute_sql_file(f"{sql_folder_name}/{file}/{t_file}")
            else:
                if file != create_file_name:
                    inexecutable_queries += await self.execute_sql_file(f"{sql_folder_name}/{file}")

        await self.execute_sql_file(f"{sql_folder_name}/metadata/{create_file_name}")
        await self.execute_sql_file(f"{sql_folder_name}/constraints/{create_file_name}")
        await self.execute_sql_file(f"{sql_folder_name}/views/{create_file_name}")

        async with aiofiles.open(f"{sql_folder_name}/functions/{create_file_name}", "w") as manual_file:
            await manual_file.write(inexecutable_queries)

    async def migration(self):
        """Migrate old data to the new database."""
        await self._connect_to_other_database(**{
            "host": self._db_host,
            "database": "postgres",
            "user": self._db_user,
            "password": self.__db_pass,
            "port": self._db_port
        })

        ...

    async def _connect_to_other_database(self, **kwargs):
        """Create a db connection to another database using the same credentials."""
        ...