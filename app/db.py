import sqlite3
from config import DB_NAME

class Financial_DB:
    @staticmethod
    def connect():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def get_daily_open_close_from_db(ticker, date):
        conexion = Financial_DB.connect()
        cursor = conexion.cursor()
        consulta = "SELECT * FROM daily_open_close WHERE symbol = ? AND date = ?"
        cursor.execute(consulta, (ticker, date))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado

    @staticmethod
    def save_daily_open_close_to_db(data):
        conexion = Financial_DB.connect()
        cursor = conexion.cursor()
        consulta = "INSERT INTO daily_open_close (data) VALUES (?, ?, ?)"
        cursor.execute(consulta, str(data))
        conexion.commit()
        conexion.close()
