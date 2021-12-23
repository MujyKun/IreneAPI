# IreneAPI v2.0 - A Complete Rewrite



## Self-Hosting

1) Install and create a [Postgres Server](https://www.postgresql.org/download/) 
2) Install [Python 3.8.8](https://www.python.org/downloads/release/python-388/) 
3) Install `pip` by typing ``python get-pip.py`` or  ``python -m ensurepip --upgrade`` in a terminal.
4) Install the requirements by typing ``pip install -r requirements.txt`` in a terminal in the directory with  
the `requirements.txt`.
5) Create the Database using the below SQL query: (the rest of the DB will be created on run.)
```
CREATE DATABASE bot WITH OWNER = postgres ENCODING = 'UTF8' CONNECTION LIMIT = -1;
```
6) Rename ``.env.example`` to `.env` and fill out the environment variables with your information.  
7) After the first run, all tables should have been created. Unfortunately due to parsing issues and since ORM is not being used,  
functions must be created manually and a file ``/sql/functions/create.sql`` will be created 
after the first run which you may execute.


## Contribute