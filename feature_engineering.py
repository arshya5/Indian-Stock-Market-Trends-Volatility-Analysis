import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("reliance_stock.csv")

data["Date"] = pd.to_datetime(data["Date"])
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

data = data.dropna()

# Moving averages
data["MA10"] = data["Close"].rolling(window=10).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()

print(data.head())

plt.figure(figsize=(12,6))

plt.plot(data["Date"], data["Close"], label="Close")
plt.plot(data["Date"], data["MA10"], label="MA10")
plt.plot(data["Date"], data["MA50"], label="MA50")

plt.legend()
plt.title("Moving Average - Reliance")
plt.show()
data.to_csv("reliance_features.csv", index=False)
print("Feature file saved")