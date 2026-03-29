import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.ensemble import RandomForestRegressor

import plotly.graph_objects as go
import plotly.express as px


st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")

st.title("Stock Market Analysis Dashboard")
st.caption("Exploratory Data Analysis & Forecasting (India)")

st.markdown("---")



stocks = {
    "RELIANCE": "data/RELIANCE.NS_features.csv",
    "TCS": "data/TCS.NS_features.csv",
    "INFY": "data/INFY.NS_features.csv",
    "HDFCBANK": "data/HDFCBANK.NS_features.csv",
    "ICICIBANK": "data/ICICIBANK.NS_features.csv"
}

selected_stock = st.selectbox("Select Stock", list(stocks.keys()))
file = stocks[selected_stock]

df = pd.read_csv(file)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")



st.markdown("Compare Stocks")

colA, colB = st.columns(2)

stock1 = colA.selectbox("Stock A", list(stocks.keys()), key="s1")
stock2 = colB.selectbox("Stock B", list(stocks.keys()), key="s2")

df1 = pd.read_csv(stocks[stock1])
df2 = pd.read_csv(stocks[stock2])

df1["Date"] = pd.to_datetime(df1["Date"])
df2["Date"] = pd.to_datetime(df2["Date"])



features = ["Lag1", "Lag2", "Lag3", "MA5", "MA10", "Return"]

X = df[features]
y = df["Close"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)



last_15 = df.tail(15)
actual_prices = last_15["Close"]
dates_actual = last_15["Date"].dt.strftime("%d-%b")



last_row = df.iloc[-1].copy()
future_prices = []

for i in range(15):
    input_data = pd.DataFrame([last_row[features]])
    next_price = model.predict(input_data)[0]
    future_prices.append(next_price)

    last_row["Lag3"] = last_row["Lag2"]
    last_row["Lag2"] = last_row["Lag1"]
    last_row["Lag1"] = next_price

    last_row["MA5"] = (last_row["MA5"] * 4 + next_price) / 5
    last_row["MA10"] = (last_row["MA10"] * 9 + next_price) / 10
    last_row["Return"] = (next_price - last_row["Lag2"]) / last_row["Lag2"]


last_date = pd.to_datetime(last_15["Date"].iloc[-1])
future_dates = pd.date_range(start=last_date, periods=16)[1:].strftime("%d-%b")



latest_price = actual_prices.iloc[-1]
predicted_price = future_prices[-1]
change = predicted_price - latest_price

col1, col2, col3 = st.columns(3)

col1.metric("Current Price", f"₹{round(latest_price,2)}")
col2.metric("Predicted Price", f"₹{round(predicted_price,2)}")
col3.metric("Expected Change", f"{round(change,2)}")

st.markdown("---")



col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Recent Performance")
    fig1, ax1 = plt.subplots()
    ax1.plot(dates_actual, actual_prices, marker="o")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price (INR)")
    plt.xticks(rotation=45)
    ax1.grid()
    st.pyplot(fig1)

with col2:
    st.subheader("🔮 Forecast (Next 15 Days)")
    fig2, ax2 = plt.subplots()
    ax2.plot(future_dates, future_prices, marker="o")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Predicted Price (INR)")
    plt.xticks(rotation=45)
    ax2.grid()
    st.pyplot(fig2)

st.markdown("---")



st.subheader("Exploratory Data Analysis Findings")

st.markdown("""
- Structural breaks indicate shifting market regimes  
- Volatility is event-driven and clustered  
- Returns exhibit fat tails (higher extreme risk)  
- Volatility is mean-reverting over time  
- Strong autocorrelation in price movements  
- Moving averages confirm trends but lag price  
- Weak relationship between volume and price  
- Long-term growth persists despite short-term noise  
""")

st.markdown("---")


st.subheader(" Deep Dive Analysis")

graph_option = st.selectbox(
    "Select Analysis",
    [
        "Price Trend",
        "Moving Average",
        "Returns Distribution",
        "Volatility",
        "Cumulative Returns"
    ]
)

image_folder = "eda/visualizations"

image_map = {
    "Price Trend": "price_trend.png",
    "Moving Average": "moving_average.png",
    "Returns Distribution": "returns_distribution.png",
    "Volatility": "rolling_volatility.png",
    "Cumulative Returns": "cumulative_returns.png"
}

img_path = os.path.join(image_folder, image_map[graph_option])

if os.path.exists(img_path):
    st.image(img_path, caption=graph_option)

st.markdown("---")




st.subheader("Model Output")

if predicted_price > latest_price:
    st.success("Upward trend expected based on model output")
else:
    st.error("Downward trend expected based on model output")

st.markdown("---")



st.markdown("Price Comparison")

fig = go.Figure()

fig.add_trace(go.Scatter(x=df1["Date"], y=df1["Close"], name=stock1))
fig.add_trace(go.Scatter(x=df2["Date"], y=df2["Close"], name=stock2))

st.plotly_chart(fig, use_container_width=True)



st.markdown("Risk Indicator")

volatility = df["Return"].std()

if volatility < 0.01:
    st.success("Low Risk (Stable Price Movement)")
elif volatility < 0.02:
    st.warning("Moderate Risk")
else:
    st.error("High Risk (Volatile Stock)")

st.caption("Risk derived from historical return volatility")



st.markdown("Interactive Price Trend")

fig = px.line(df, x="Date", y="Close", title="Stock Price Over Time")

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
)

st.plotly_chart(fig, use_container_width=True)