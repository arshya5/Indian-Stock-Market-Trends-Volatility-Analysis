import pandas as pd

stocks = [
    "RELIANCE.NS.csv",
    "TCS.NS.csv",
    "INFY.NS.csv",
    "HDFCBANK.NS.csv",
    "ICICIBANK.NS.csv"
]

for file in stocks:

    print("Processing:", file)

    df = pd.read_csv(file)

    # Convert Close to numeric
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # Moving averages
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA50"] = df["Close"].rolling(50).mean()

    # Return %
    df["Return"] = df["Close"].pct_change()

    # Drop null rows
    df = df.dropna()

    new_name = file.replace(".csv", "_features.csv")

    df.to_csv(new_name, index=False)

    print("Saved:", new_name)

print("Feature engineering completed")