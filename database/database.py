import sqlite3
from contextlib import closing


def create_database():
    with closing(sqlite3.connect('database.db')) as conn:
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
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
        CREATE TABLE IF NOT EXISTS TodayMenu(
        id INTEGER PRIMARY KEY,
        name VARCHAR(256) UNIQUE NOT NULL,
        text VARCHAR(256) NOT NULL
        )
        ''')

        conn.commit()


if __name__ == '__main__':
    create_database()