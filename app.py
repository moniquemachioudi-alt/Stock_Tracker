
# Local URL: http://localhost:8501
# Network URL: http://192.168.1.179:8501

import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Tracker")

# Input box
ticker = st.text_input("Enter a stock ticker (e.g., AAPL)")

if ticker:
    try:
        # Fetch stock data
        stock = yf.Ticker(ticker)
        data = stock.history(period="2d")

        if len(data) >= 2:
            # Prices
            latest_price = data["Close"].iloc[-1]
            prev_close = data["Close"].iloc[-2]
            percent_change = ((latest_price - prev_close) / prev_close) * 100

            # Display in Streamlit
            st.metric(
                label=f"{ticker.upper()} Price",
                value=f"${latest_price:.2f}",
                delta=f"{percent_change:.2f}%"
            )

            # Optional: line chart
            st.line_chart(data["Close"])
        else:
            st.write("Not enough data to calculate change.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
