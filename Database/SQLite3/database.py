"""
database_setup.py

This file contains a script to set up an SQLite database for storing dictionary data.
It creates the necessary tables and inserts initial data for further program functionality.

The database structure includes the "Themes", "Notes", and "Settings" tables with their respective fields.

After establishing a connection to the database, the code creates the required tables, inserts initial data
into the "Settings" table, and saves the changes in the database.

Note: Before running this script, make sure the "dictionary_data.sqlite" database file
and the "Database/SQLite3" directory exist.
"""

import sqlite3

try:
    connection = sqlite3.connect("Database/SQLite3/dictionary_data.sqlite")
    cursor = connection.cursor()

    create_table_themes = """
        CREATE TABLE IF NOT EXISTS Themes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            theme VARCHAR(50) NOT NULL
        )
    """
    cursor.execute(create_table_themes)

    create_table_notes = """
        CREATE TABLE IF NOT EXISTS Notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word VARCHAR(30) NOT NULL,
            translate VARCHAR(30) NOT NULL,
            themes_id INTEGER,
            FOREIGN KEY (themes_id) REFERENCES Themes(id)
        )
    """
    cursor.execute(create_table_notes)

    create_table_save_settings = """
        CREATE TABLE IF NOT EXISTS Settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            theme VARCHAR(50),
            verify INTEGER,
            repetition INTEGER,
            word INTEGER,
            translate INTEGER,
            randomly INTEGER,
            successively INTEGER,
            timer INTEGER
        )
    """
    cursor.execute(create_table_save_settings)

    main_save = """
        INSERT INTO Settings (
            theme,
            verify,
            repetition,
            word,
            translate,
            randomly,
            successively,
            timer
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    values = ("List of themes", 1, 0, 1, 0, 1, 0, 5)
    cursor.execute(main_save, values)

    connection.commit()
    connection.close()

except sqlite3.Error as error:
    print(f"Error executing CREATE query: {error}")
