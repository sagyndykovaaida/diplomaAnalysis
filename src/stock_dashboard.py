import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

# Set the title of the web app
st.title('Stock Dashboard')

# Input fields in the sidebar for user input
ticker = st.sidebar.text_input('Ticker', 'AAPL')  # Default ticker is Apple
start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2022-01-01'))
end_date = st.sidebar.date_input('End Date', pd.to_datetime('today'))

# Function to fetch and return stock data
def load_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

# Load data
data = load_data(ticker, start_date, end_date)

# Display the first 5 rows of the data
st.write("Showing data for:", ticker)
st.dataframe(data.head())

# Plotting the Closing Price
fig = px.line(data, x='Date', y='Close', title=f'Closing Price of {ticker}')
st.plotly_chart(fig)

# Display additional statistics
st.write("Statistics:")
st.write(data.describe())
