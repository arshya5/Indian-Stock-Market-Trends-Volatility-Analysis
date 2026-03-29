

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


stocks = [
    "data/RELIANCE.NS_features.csv",
    "data/TCS.NS_features.csv",
    "data/INFY.NS_features.csv",
    "data/HDFCBANK.NS_features.csv",
    "data/ICICIBANK.NS_features.csv"
]


results = []

for file in stocks:

    df = pd.read_csv(file)

    X = df[["Lag1", "Lag2", "Lag3"]]
    y = df["Close"]

    split = int(len(df) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    results.append({
        "Stock": file.split("/")[1].split("_")[0],
        "RMSE": round(rmse, 2),
        "MAE": round(mae, 2),
        "R2": round(r2, 2)
    })




results_df = pd.DataFrame(results)

print("\n=== MODEL PERFORMANCE SUMMARY ===\n")
print(results_df)




best_stock = results_df.sort_values(by="R2", ascending=False).iloc[0]

print("\nBest Performing Stock:")
print(best_stock)