import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("reliance_stock.csv")


data["Date"] = pd.to_datetime(data["Date"])


data["Close"] = pd.to_numeric(data["Close"], errors="coerce")


data = data.dropna()

plt.figure(figsize=(12,6))

plt.plot(data["Date"], data["Close"])

plt.title("Reliance Stock Closing Price (2015–2024)")
plt.xlabel("Date")
plt.ylabel("Price (INR)")

plt.grid(True)

plt.tight_layout()

plt.show()