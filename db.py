import sqlite3


def create_table():
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id TEXT,
        username TEXT,
        first_name TEXT,
        last_name TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(telegram_id, username, first_name, last_name):
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", (telegram_id, username, first_name, last_name))

    conn.commit()
    conn.close()
