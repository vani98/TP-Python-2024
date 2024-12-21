import sqlite3
import pandas as pd
from config import DB_NAME

class Financial_DB:
    @staticmethod
    def connect():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def get_daily_open_close_from_db(ticker, date):
        connection = Financial_DB.connect()
        query = "SELECT * FROM daily_open_close WHERE ticker = ? AND date = ?"
        result = pd.read_sql_query(query, connection, params=(ticker, date))
        connection.close()
        return result
    
    @staticmethod
    def get_all_day_daily_open_close_from_db(date):
        connection = Financial_DB.connect()
        query = "SELECT * FROM daily_open_close WHERE date = ?"
        result = pd.read_sql_query(query, connection, params=(date,))
        connection.close()
        return result
    
    @staticmethod
    def save_daily_open_close_to_db(data):
        query = """
        INSERT OR REPLACE INTO daily_open_close (date, ticker, open, close, high, low, volume, afterHours, preMarket) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        with Financial_DB.connect() as connection:
            data_row = data.iloc[0]  # Accedemos directamente a la primera fila
            connection.execute(query, tuple(data_row))  # Ejecutamos la consulta pasando los valores como tupla
            connection.commit()


