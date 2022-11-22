import sqlite3


class User:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM "users" WHERE user_id="{user_id}"').fetchall()
            return bool(len(result))

    def user_add(self, user_id, user_username, user_fullname):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id', 'user_username', 'user_fullname') "
                                       "VALUES (?, ?, ?)", (user_id, user_username, user_fullname))
