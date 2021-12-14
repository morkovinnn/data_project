import sqlite3

class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с базой данных"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем существование пользователя в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Получаем id юзера в базе по его telegram_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавление пользователя в базу данных"""
        self.cursor.execute("INSERT INTO `users` (`users_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_name(self, user_id, users_name):
        """Добавляем имя друга"""
        self.cursor.execute("INSERT INTO `records` (`users_id`, `users_name` VALUES (?,?)",
                            (self.get_user_id(user_id),
                             operation == '+',
                             users_name))
        return self.conn.commit()

    def get_records(self, user_id):
        """Получаем все записи друзей"""
        result = self.cursor.execute("SELECT * FROM `records` WHERE `user_id` = ? ORDER BY `date`",
                                     self.get_user_id(user_id))
        return result.fetchall()


    def close(self):
        """Закрытие работы с базой"""
        self.conn.close()
