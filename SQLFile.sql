CREATE DATABASE financial_data

CREATE TABLE stock_prices (
    date TEXT NOT NULL PRIMARY KEY, 
    open REAL NOT NULL,
    close REAL NOT NULL,
    high REAL NOT NULL,
    low REAL NOT NULL,
    volume INTEGER NOT NULL,
    afterHours REAL,
    preMarket REAL,
);