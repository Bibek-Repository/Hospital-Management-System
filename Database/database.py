import sqlite3

def init_db():
    conn = sqlite3.connect('patient_information.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()