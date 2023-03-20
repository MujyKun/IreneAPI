# IreneAPI v2.0 - A Complete Rewrite



## Self-Hosting

1) Install and create a [Postgres Server](https://www.postgresql.org/download/) 
2) Install [Python 3.9.9](https://www.python.org/downloads/release/python-399/) 
3) Install `pip` by typing ``python get-pip.py`` or  ``python -m ensurepip --upgrade`` in a terminal.
4) Install the requirements by doing one of the below steps.
   1) Typing ``pip install -r requirements.txt`` in a terminal in the directory with  
   the `requirements.txt`.
   2) If you have poetry installed, type ``poetry install`` in a terminal in the directory with  
   the `pyproject.toml`.
5) Create the Database using the below SQL query: (the rest of the DB will be created on run.)
```
CREATE DATABASE bot WITH OWNER = postgres ENCODING = 'UTF8' CONNECTION LIMIT = -1;
```
6) Rename ``.env.example`` to `.env` and fill out the environment variables with your information.  
7) After the first run, all tables should have been created. Unfortunately due to parsing issues and since ORM is not being used,  
functions must be created manually and a file ``/sql/functions/create.sql`` will be created 
after the first run which you may execute. The parsing issues will be fixed at a later time.
8) To run the SQL files, you can use `psql -U postgres -d bot -f create.sql` when in the appropriate directory (sql/functions).  
9) To run the API with a setup configuration & poetry, use one of the following:
   1) `poetry run python -m hypercorn --config .\hypercorn.toml run:app`
   2) `poetry run python3 -m hypercorn --config .\hypercorn.toml run:app`
   3) `poetry run python3 -m hypercorn --bind '0.0.0.0:5454' --workers=25 run:app`  


### Adding Google Drive [These are instructions for a Google Workplace administrator account]
1) [Create a service account](https://console.cloud.google.com/apis/api/drive.googleapis.com/).
2) Create keys for the service account
3) Download the keys as a json file.
4) Rename the json file to `service_account.json` and put it in the root folder.
5) Go to the [workplace admin console](https://admin.google.com/)
6) Go to Main Menu -> Show More -> Security -> Access and data control -> API Controls
7) Select `Manage Domain Wide Delegation` in the `Domain wide delegation` pane.
8) Click `Add New` and enter the service account's Client ID. 
9) In the OAuth scopes field, enter `https://www.googleapis.com/auth/drive` and then click Authorize.
10) Edit the json file and add a key `subject` with the value of the user email you want to connect to. EX: ("subject": "mujy@irenebot.com")

## Contribute

## Development Guidelines

- The API will only query functions or views from the database. The views and functions may provide specific information and may leave out unnecessary information.  
**Example:** 
```sql
-- A table x has columns a, b, and c
-- A view may provide the following query:
SELECT a, b FROM x;

-- The view should never specify all columns with *
-- DO NOT:
SELECT * FROM x;

-- DO:
SELECT a, b, c FROM x;

-- Assuming the queries below are in a view called y
-- The API may manipulate the views as needed.
SELECT a, b FROM y;
SELECT * FROM y;

-- Doing it this way will allow the API to remain consistent with 
-- how it queries and returns data.

-- The only exceptions to this are dynamic internal functions (that must also be prefixed with an underscore) and standalone applications.
```