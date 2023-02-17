import sqlite3 as sq
with sq.connect('users.db') as con:
    cur = con.cursor()
    # cur.execute('''CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age>15 AND age<70),
    # email TEXT UNIQUE
    # )''')

    cur.execute("""
    DROP TABLE person_table
    """)

