import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

st.title("Indian Stock Market Prediction")

data = pd.read_csv("reliance_features.csv")

data = data.dropna()

X = data[["MA10", "MA50"]]
y = data["Close"]

model = LinearRegression()
model.fit(X, y)

st.write("Enter Moving Average values")

ma10 = st.number_input("MA10")
ma50 = st.number_input("MA50")

if st.button("Predict"):

    pred = model.predict([[ma10, ma50]])

    st.success(f"Predicted Price: {pred[0]:.2f}")