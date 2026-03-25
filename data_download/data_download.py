import yfinance as yf
import pandas as pd

ticker = "RELIANCE.NS"

data = yf.download(ticker, start="2015-01-01", end="2024-01-01")


data.reset_index(inplace=True)

print(data.head())

data.to_csv("reliance_stock.csv", index=False)

print("Data saved successfully")