# TP-Python-2024
Trabajo final de Python en ITBA.

## Instalación del proyecto
jupyterlab==4.2.5jupyterlab==4.2.5
```
conda create -n TP-Final-Python-2024
conda activate TP-Final-Python-2024
conda install python==3.10.13 jupyterlab==4.2.5
pip install -r requirements.txt
```

## Cómo correr la aplicación

### App terminal

```
python ./app/terminal_app.py
```


### App Web

```
streamlit run ./app/web_app.py
```

## Cómo crear la BD

En la consola creamos la db
```
sqlite3 financial_data.db
```
Luego creamos la data table
```
.schema 
CREATE TABLE daily_open_close (
    date TEXT NOT NULL, 
    ticker TEXT NOT NULL,
    open REAL NOT NULL,
    close REAL NOT NULL,
    high REAL NOT NULL,
    low REAL NOT NULL,
    volume REAL NOT NULL,
    afterHours REAL NOT NULL,
    preMarket REAL NOT NULL,
    PRIMARY KEY (date, ticker)
);
```
Datos para probar

```
INSERT INTO daily_open_close (date, symbol, open, close, high, low, volume, afterHours, preMarket) 
VALUES ('2023-01-09', 'MSFT', 300.0, 305.0, 310.0, 295.5, 15000000, 303.5, 302.0);

INSERT INTO daily_open_close (date, symbol, open, close, high, low, volume, afterHours, preMarket) 
VALUES ('2023-01-09', 'TSLA', 600.0, 610.0, 620.0, 590.0, 20000000, 608.5, 607.0);

INSERT INTO daily_open_close (date, symbol, open, close, high, low, volume, afterHours, preMarket) 
VALUES ('2023-01-09', 'AMZN', 100.0, 105.0, 110.0, 95.0, 13000000, 104.5, 103.5);
```