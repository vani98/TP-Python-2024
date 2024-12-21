import matplotlib.pyplot as plt
from datetime import datetime
from db import Financial_DB

def validate_date(date_str):
    try:
        # Intenta convertir la fecha en el formato YYYY-MM-DD
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_date_input():
    date = ""
    while not validate_date(date):
        date = input("Ingrese una fecha en el formato YYYY-MM-DD: ")
        if not validate_date(date):
            print("Fecha inválida. Intente nuevamente.")
    return date

def show_img(df):
    if len(df) > 1:
        labels = []
        prices_diffs = []

        for row in df.itertuples():
            labels.append(row.ticker)
            prices_diffs.append(row.open - row.close)
        width = 0.5
        x = range(len(df))
        plt.figure(figsize=(10, 6))
        plt.bar(x, prices_diffs, width, label='Price Difference', color='blue')
        plt.xlabel('Ticker')
        plt.ylabel('Diferencia de valor')
        plt.title('Comparación Stock Prices')
        plt.xticks(x, labels)
        plt.legend()
        plt.tight_layout()

        file_name = f"grafico_{df.iloc[0].date}.png"
        file_path = f"img/{file_name}"

        plt.savefig(file_path)
        print(f"Gráfico de diferencia de valores generado en: {file_path}")

    else:
        print("Consulte más tickers con el día seleccionado para la creación del gráfico de diferencia de valores.")

def print_all_day_data(date):
    all_days = Financial_DB()
    data = all_days.get_all_day_daily_open_close_from_db(date) 
    if not data.empty:
        show_img(data)
    else:
        print("No se encontraron datos para graficar.")
