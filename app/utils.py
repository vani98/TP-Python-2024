from datetime import datetime

def validate_date(date_str):
    try:
        # Intenta convertir la fecha en el formato YYYY-MM-DD
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
