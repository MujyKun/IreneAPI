import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
env_path = parent_dir / '.env'
load_dotenv(dotenv_path=env_path)

db_kwargs = {
    'dbname': os.getenv("POSTGRES_DATABASE"),
    'user': os.getenv("POSTGRES_USER"),
    'password': os.getenv("POSTGRES_PASSWORD"),
    'host': os.getenv("POSTGRES_HOST"),
    'port': os.getenv("POSTGRES_PORT")
}


def delete_old_api_logs():
    with psycopg2.connect(**db_kwargs) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM public.apiusage au WHERE au.time < CURRENT_DATE - INTERVAL '7 days';"
            cursor.execute(delete_query)


if __name__ == '__main__':
    from time import sleep
    while True:
        print("Deleting Old API logs.")
        delete_old_api_logs()
        print("Deleted Old API Logs - Sleeping")
        sleep(86400*7)
