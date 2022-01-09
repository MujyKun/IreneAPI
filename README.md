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


## Contribute

## Development Guide

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

```