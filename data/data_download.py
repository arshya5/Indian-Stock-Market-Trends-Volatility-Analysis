import yfinance as yf
import pandas as pd

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

start_date = "2015-01-01"
end_date = "2024-01-01"

for stock in stocks:

    print("Downloading", stock)

    data = yf.download(
        stock,
        start=start_date,
        end=end_date
    )

    filename = f"{stock}.csv"

    data.to_csv(filename)

    print("Saved:", filename)

print("All stock data downloaded")