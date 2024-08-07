import sqlite3

conn = sqlite3.connect('messages.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
''')
conn.commit()
conn.close()
