

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style='whitegrid')

# Create visualization folder
os.makedirs("eda/visualizations", exist_ok=True)



df = pd.read_csv('data/RELIANCE.NS_features.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("\nDataset Loaded Successfully\n")




print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIPTION ---")
print(df.describe())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())




plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Close'])
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.tight_layout()
plt.savefig("eda/visualizations/price_trend.png")
plt.show()




plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close')
plt.plot(df['MA5'], label='MA5')
plt.plot(df['MA10'], label='MA10')
plt.legend()
plt.title('Moving Averages')
plt.tight_layout()
plt.savefig("eda/visualizations/moving_average.png")
plt.show()




plt.figure(figsize=(8,5))
sns.histplot(df['Return'], bins=50, kde=True)
plt.title('Returns Distribution')
plt.tight_layout()
plt.savefig("eda/visualizations/returns_distribution.png")
plt.show()




plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Return'])
plt.title('Daily Returns Over Time')
plt.xlabel('Date')
plt.ylabel('Return')
plt.tight_layout()
plt.savefig("eda/visualizations/returns_over_time.png")
plt.show()




df['Cumulative_Return'] = (1 + df['Return']).cumprod()

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Cumulative_Return'])
plt.title('Cumulative Returns (Growth of ₹1)')
plt.xlabel('Date')
plt.ylabel('Growth')
plt.tight_layout()
plt.savefig("eda/visualizations/cumulative_returns.png")
plt.show()




volatility = df['Return'].std()
print("\nVolatility:", round(volatility, 4))




df['Rolling_Volatility'] = df['Return'].rolling(window=10).std()

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Rolling_Volatility'])
plt.title('Rolling Volatility (10-Day)')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.tight_layout()
plt.savefig("eda/visualizations/rolling_volatility.png")
plt.show()




plt.figure(figsize=(8,6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig("eda/visualizations/correlation.png")
plt.show()




plt.figure(figsize=(8,5))
plt.scatter(df['Volume'], df['Close'])
plt.title('Volume vs Price')
plt.xlabel('Volume')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig("eda/visualizations/volume_vs_price.png")
plt.show()




df['Price_Change'] = df['Close'].diff()

plt.figure(figsize=(8,5))
plt.scatter(df['Price_Change'], df['Volume'])
plt.title('Price Change vs Volume')
plt.xlabel('Price Change')
plt.ylabel('Volume')
plt.tight_layout()
plt.savefig("eda/visualizations/price_change_vs_volume.png")
plt.show()




df['Trend'] = df['Close'].rolling(20).mean()

plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Price')
plt.plot(df['Trend'], label='20-Day Trend')
plt.legend()
plt.title('Trend Identification')
plt.tight_layout()
plt.savefig("eda/visualizations/trend_regime.png")
plt.show()




print("\n=== KEY INSIGHTS ===")

print("\n1. Trend Behavior:")
print("Stock exhibits long-term trends with periodic corrections.")

print("\n2. Volatility:")
print("Volatility is clustered, indicating periods of market instability rather than randomness.")

print("\n3. Returns:")
print("Daily returns are mostly centered around zero, suggesting moderate day-to-day changes.")

print("\n4. Volume Behavior:")
print("Large price movements are often accompanied by high trading volume.")

print("\n5. Investment Insight:")
print("Cumulative returns show how investment grows over time, highlighting long-term potential.")

print("\n6. Trend Regimes:")
print("Moving averages help identify bullish and bearish phases in the market.")


print("\nEDA Completed Successfully ✅")