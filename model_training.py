import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

data = pd.read_csv("reliance_features.csv")

data = data.dropna()

X = data[["MA10", "MA50"]]
y = data["Close"]

model = LinearRegression()

model.fit(X, y)

predictions = model.predict(X)

plt.figure(figsize=(12,6))

plt.plot(y.values, label="Real")
plt.plot(predictions, label="Predicted")

plt.legend()

plt.title("Stock Price Prediction (Linear Regression)")
plt.xlabel("Days")
plt.ylabel("Price")

plt.show()