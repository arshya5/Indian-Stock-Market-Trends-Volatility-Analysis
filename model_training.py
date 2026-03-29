import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


stocks = [
    "RELIANCE.NS_features.csv",
    "TCS.NS_features.csv",
    "INFY.NS_features.csv",
    "HDFCBANK.NS_features.csv",
    "ICICIBANK.NS_features.csv"
]


for file in stocks:

    print("\nTraining model for:", file)

    df = pd.read_csv(file)

    # Features
    X = df[["MA10", "MA50", "Return"]]

    # Target
    y = df["Close"]

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Model
    model = LinearRegression()

    model.fit(X_train, y_train)

    # Prediction
    predictions = model.predict(X_test)

    # Error
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    print("RMSE:", rmse)