import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
from config import DB_NAME

class Financial_DB:
    @staticmethod
    def connect():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def get_mensual(date):
        connection = Financial_DB.connect()
        query = "SELECT * FROM daily_open_close WHERE date = ?"
        result = pd.read_sql_query(query, connection, params=(date))
        connection.close()
        return result

