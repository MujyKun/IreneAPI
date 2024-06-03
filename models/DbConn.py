from os import listdir
from os.path import isdir, exists
import aiofiles
import asyncpg.exceptions


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

    async def connect(self):
        """Connect to the PostgreSQL Database."""

        await self._create_pool(
            **{
                "host": self._db_host,
                "database": self._db_name,
                "user": self._db_user,
                "password": self.__db_pass,
                "port": self._db_port,
            }
        )
        await self.update_db_structure()
        print(f"Connected to Database {self._db_name} as {self._db_user}.")

    async def execute_sql_file(self, file_path: str, use_terminal=False) -> str:
        """Read and execute the queries in a SQL file.

        :param file_path: str
            File name to read and execute.
        :param use_terminal: bool
            Whether to use the terminal for auto executing create files.
        :returns str:
            Code that cannot be executed.
        """
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

    async def update_db_structure(self, use_terminal=True, use_ddl=True):
        """
        Attempt to create/update the DB structure.

        :param use_terminal: Whether to use the terminal to run the sql scripts
        :param use_ddl: Whether to also use ddl scripts to create the database at the start.
        """
        sql_folder_name = "sql"
        create_file_name = "create.sql"
        ddl_file_name = "database.ddl"
        inexecutable_function_queries = ""
        inexecutable_view_queries = ""
        execute_later = ["metadata", "constraints"]
        ddl_file_path = f"{sql_folder_name}/{ddl_file_name}"
        if use_ddl and exists(ddl_file_path):
            await self.execute_sql_file(ddl_file_path, use_terminal=use_terminal)

        for file in listdir(sql_folder_name):
            if file in execute_later:
                continue

            if isdir(f"{sql_folder_name}/{file}"):
                # run the create files first.
                if file not in ["functions", "views"]:
                    create_file = f"{sql_folder_name}/{file}/{create_file_name}"
                    inexecutable_function_queries += await self.execute_sql_file(
                        create_file
                    )

                for t_file in listdir(f"{sql_folder_name}/{file}"):
                    if t_file != create_file_name:
                        data = await self.execute_sql_file(
                            f"{sql_folder_name}/{file}/{t_file}"
                        )
                        if file == "functions":
                            inexecutable_function_queries += data
                        elif file == "views":
                            inexecutable_view_queries += data
            else:
                if file != create_file_name:
                    inexecutable_function_queries += await self.execute_sql_file(
                        f"{sql_folder_name}/{file}"
                    )

        async with aiofiles.open(
            f"{sql_folder_name}/functions/{create_file_name}", "w"
        ) as manual_file:
            await manual_file.write(inexecutable_function_queries)

        async with aiofiles.open(
            f"{sql_folder_name}/views/{create_file_name}", "w"
        ) as manual_file:
            await manual_file.write(inexecutable_view_queries)

        await self.execute_sql_file(
            f"{sql_folder_name}/metadata/{create_file_name}", use_terminal=use_terminal
        )
        await self.execute_sql_file(
            f"{sql_folder_name}/constraints/{create_file_name}", use_terminal=use_terminal
        )
        await self.execute_sql_file(
            f"{sql_folder_name}/views/{create_file_name}", use_terminal=use_terminal
        )
        # await self.execute_sql_file(f"{sql_folder_name}/functions/{create_file_name}", use_terminal=True)

    async def get_connection(self):
        """Get a new pool connection.

        This is a connection built manually.
        It must be released/closed using the close_connection method.
        """
        ...

    async def close_connection(self, connection):
        """Releases a connection."""
        ...
