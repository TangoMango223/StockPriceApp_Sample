import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of GOOGL, Google!

""")

# Define ticker symbol
tickersymbol = "GOOGL"
tickerData = yf.Ticker(tickersymbol)

# Get historical data
tickerDF = tickerData.history(period = '1d', start = '2020-1-01', end = '2024-1-01')
# Order is: OPEN HIGH LOW CLOSE VOLUME DIVIDENDS STOCK SPLITS

# Chart this on Streamlit
st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)

st.write("""

> Christine says, "Studying 10 hours a day is hard. But failing a course is even worse.
""")

st.write(f"""

## Here's a table:

| Syntax      | {tickersymbol} |
| ----------- | ----------- |
| Hi | There |
| Paragraph | Text | 

""")
