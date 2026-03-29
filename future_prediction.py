import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


file = "RELIANCE.NS_features.csv"

df = pd.read_csv(file)


X = df[["MA10", "MA50", "Return"]]
y = df["Close"]


model = LinearRegression()
model.fit(X, y)



last_row = df.iloc[-1]

ma10 = last_row["MA10"]
ma50 = last_row["MA50"]
ret = last_row["Return"]
last_close = last_row["Close"]


future_days = 5

future_prices = []


for i in range(future_days):

    input_data = np.array([[ma10, ma50, ret]])

    next_price = model.predict(input_data)[0]

    future_prices.append(next_price)

    
    last_close = next_price
    ret = (next_price - ma10) / ma10

    ma10 = (ma10 * 9 + next_price) / 10
    ma50 = (ma50 * 49 + next_price) / 50


print("\nFuture Predictions (Next 5 Days):")

for i, price in enumerate(future_prices, start=1):
    print(f"Day {i}: {round(price, 2)}")