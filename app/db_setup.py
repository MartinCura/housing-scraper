#!/usr/bin/env python3
import sqlite3


SQLITE_DB_FILE = "data/properties.sqlite"


def create_connection(db_file):
    """Create connection to SQLite database specified by db_file

    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return None


def execute(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        c.close()
    except Exception as e:
        print(e)


sql_create_properties_table = """
    CREATE TABLE IF NOT EXISTS properties (
        id integer              PRIMARY KEY,
        internal_id text        NOT NULL,
        provider text           NOT NULL,
        url text                NOT NULL,
        captured_date integer   DEFAULT CURRENT_TIMESTAMP
    );
"""

sql_create_index_on_properties_table = """
    CREATE INDEX  properties_internal_provider
    ON            properties (internal_id, provider);
"""


conn = create_connection(SQLITE_DB_FILE)

with conn:
    if conn:
        # create properties table
        execute(conn, sql_create_properties_table)
        # create properties indexes
        execute(conn, sql_create_index_on_properties_table)
        print("Database successfully set up")
    else:
        print("Error! Could not create the database connection.")
