import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


stocks = [
    "RELIANCE.NS_features.csv",
    "TCS.NS_features.csv",
    "INFY.NS_features.csv",
    "HDFCBANK.NS_features.csv",
    "ICICIBANK.NS_features.csv"
]


for file in stocks:

    print("Plotting:", file)

    df = pd.read_csv(file)

    # Use Date only if clean
    if "Date" in df.columns:
        try:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            x_axis = df["Date"]
        except:
            x_axis = range(len(df))
    else:
        x_axis = range(len(df))

    X = df[["MA10", "MA50", "Return"]]
    y = df["Close"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    x_test = list(x_axis)[-len(y_test):]

    stock_name = file.replace("_features.csv", "")

    plt.figure(figsize=(12, 6))

    plt.plot(x_test, y_test.values, label="Actual Price", linewidth=2)
    plt.plot(x_test, predictions, label="Predicted Price", linewidth=2)

    plt.title(f"Stock Price Prediction - {stock_name}", fontsize=16, fontweight="bold")

    plt.xlabel("Time Steps", fontsize=12)
    plt.ylabel("Stock Price (INR)", fontsize=12)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()