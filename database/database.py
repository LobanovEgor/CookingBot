import sqlite3
from contextlib import closing


def create_database():
    with closing(sqlite3.connect('database.db')) as conn:
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        telegram_id INTEGER PRIMARY KEY,
        isAdmin BOOLEAN NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Food(
        id INTEGER PRIMARY KEY,
        name VARCHAR(256) UNIQUE NOT NULL,
        text VARCHAR(256) NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Favorites(
        user_id INTEGER NOT NULL,
        food_id INTEGER NOT NULL,
        PRIMARY KEY(user_id, food_id),
        FOREIGN KEY (user_id) REFERENCES Users(id),
        FOREIGN KEY (food_id) REFERENCES Food(id))
        ''')

        cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_food ON Food(name)
                ''')
        cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_user_food ON Favorites(user_id)
                ''')


        conn.commit()

async def insert_user(telegram_id: int, isAdmin: bool):
    with closing(sqlite3.connect('database.db')) as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT OR IGNORE INTO Users (telegram_id, isAdmin) VALUES (?, ?)''', (telegram_id, isAdmin))
        conn.commit()


async def insert_food(name, text):
    with closing(sqlite3.connect('database.db')) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT OR IGNORE INTO Food(name, text) VALUES (?, ?)
        ''', (name, text))
        conn.comit()

async def add_favorite(telegram_id, food_name):
    with closing(sqlite3.connect('database.db')) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT id FROM Users WHERE telegram_id = ?
        ''', (telegram_id, ))
        user_id = cursor.fetchone()[0]
        cursor.execute('''
                SELECT id FROM Food WHERE name = ?
                ''', (food_name,))
        food_id = cursor.fetchone()[0]

        cursor.execute('''
        INSERT OR IGNORE INTO Favorite(user_id, food_id) VALUES (?, ?)
        ''', (user_id, food_id))

        conn.commit()

if __name__ == '__main__':
    create_database()