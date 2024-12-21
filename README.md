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
streamlit run ./app/web_app.py.py
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
    symbol TEXT NOT NULL,
    open REAL NOT NULL,
    close REAL NOT NULL,
    high REAL NOT NULL,
    low REAL NOT NULL,
    volume INTEGER NOT NULL,
    afterHours REAL NOT NULL,
    preMarket REAL NOT NULL,
    PRIMARY KEY (date, symbol)
);
```