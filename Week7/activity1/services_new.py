import sqlite3


class DBConnector:
    __instance = None
    __conn = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__conn = sqlite3.connect('app.db')
        return cls.__instance

    def get_connection(self):
        return self.__conn


class UserService:
    def get_user(self, user_id):
        conn = DBConnector().get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        return result
    

class OrderService:
    def get_orders(self, user_id):
        conn = DBConnector().get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
        result = cursor.fetchall()
        return result
    