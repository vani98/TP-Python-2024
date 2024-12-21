from utils import validate_date
from db import Financial_DB
from api_client import Finance_API

class TerminalApp:
    def __init__(self):
        self.loop = True

    def start(self):
        while self.loop:
            ticker = input("Ingrese ticker a consultar: ")
            date = input("Ingrese fecha a consultar en formato yyyy-MM-dd: ")

            if not validate_date(date):
                print("La fecha ingresada es inválida, ingrese una fecha en formato yyyy-MM-dd ej. (2022-11-20)")
                continue

            data = Financial_DB.get_daily_open_close_from_db(ticker, date)
            if data:
                print(f"Datos obtenidos de la BD: {data}")
            else:
                print("Datos no encontrados en la BD. Consultando a la API...")
                data = Finance_API.get_daily_open_close(ticker, date)
                if data:
                    print(f"Datos obtenidos de la API: {data}")
                    Financial_DB.save_daily_open_close_to_db(data)
                    print("Datos guardados con éxito.")
                else:
                    print("No se pudieron obtener datos de la API. Por favor, intente nuevamente")
            another_date = input("¿Desea consultar otra fecha? (SI/NO): ").strip().upper()
            if another_date != "SI":
                print("Consulta finalizada.")
                self.loop = False

if __name__ == "__main__":
    app = TerminalApp()
    app.start()