from utils import validate_date_input, print_all_day_data
from db import Financial_DB
from tabulate import tabulate
from api_client import Finance_API

class TerminalApp:
    def __init__(self):
        self.loop = True
    
    def start(self):
        while self.loop:
            ticker = input("Ingrese ticker a consultar: ").upper() # AAPL
            date = validate_date_input()
            # ticker = "AAPL"
            # date = "2023-01-14"

            try:
                data = Financial_DB.get_daily_open_close_from_db(ticker, date)
            except Exception as e:
                print("No se ha podido realizar la consulta en la BD.")
                print(e)
                data = None

            if data is not None and not data.empty:
                print(f"Datos obtenidos de la BD.")
                print(tabulate(data, headers='keys', tablefmt='pretty', showindex=False))
                print_all_day_data(date)
            else:
                print("Datos no encontrados en la BD. Consultando a la API...")
                try:
                    data = Finance_API.get_daily_open_close(ticker, date)
                except Exception as e:
                    print("No se pudo realizar la consulta a la API, por favor introduzca otros parámetros.")
                    print(e)
                    continue
                if not data.empty:
                    print(tabulate(data, headers='keys', tablefmt='pretty', showindex=False))
                    Financial_DB.save_daily_open_close_to_db(data)
                    print("Datos guardados con éxito.")
                    print_all_day_data(date)
                else:
                    print("No se pudieron obtener datos de la API. Por favor, intente nuevamente.")
                    continue
            
            another_date = input("¿Desea seguir consultando? (SI/NO): ").strip().upper()
            if another_date != "SI":
                print("Consulta finalizada.")
                self.loop = False

if __name__ == "__main__":
    app = TerminalApp()
    app.start()