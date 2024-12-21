import requests
import pandas as pd
# from tabulate import tabulate
from config import OPEN_CLOSE_URL, OPTIONS

class Finance_API:
    @staticmethod
    def get_daily_open_close(ticker,date):
        # URL de la API con la fecha y la API_KEY
        url = f"{OPEN_CLOSE_URL}{ticker}/{date}{OPTIONS}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "OK":
                filtered_data = {
                    "date": data.get("from"),
                    "ticker": data.get("symbol"),
                    "open": data.get("open"),
                    "close": data.get("close"),
                    "high": data.get("high"),
                    "low": data.get("low"),
                    "afterHours": data.get("afterHours"),
                    "preMarket": data.get("preMarket"),
                    "volume": data.get("volume")
                }
                return pd.DataFrame([filtered_data])
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

# api1 = Finance_API()
# datos= api1.get_daily_open_close("AAPL","2023-10-10")


# if not datos.empty:
#     print("Datos obtenidos de la API:")
#     print(tabulate(datos, headers='keys', tablefmt='pretty', showindex=False))
# else:
#     print("No se encontraron datos para la fecha proporcionada.")