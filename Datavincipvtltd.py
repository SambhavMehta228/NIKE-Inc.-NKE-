# Import the yfinance, pandas, and plotly libraries.
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Download the intraday data for NKE for the past year with Data in interval of 1 Day.
intraday_data = yf.download(tickers="NKE", period="1y", interval="1d", auto_adjust=True)
#Print the Data Type of Downloaded Data .
print(type(intraday_data))

# Print the rows of the data.
print(intraday_data.head)

# Print the column names of the data.
print(intraday_data.columns)

# Display information about the data.
print(intraday_data.info())

# Print the maximum and minimum dates in the data.
print(intraday_data.index.max())
print(intraday_data.index.min())

# Print the average daily trading volume.
print("Average Day Trading Volume : ", intraday_data.Volume.mean())

# Create a candlestick chart of the data.
fig = go.Figure(data=[go.Candlestick(x=intraday_data.index, open=intraday_data.Open, high=intraday_data.High, low=intraday_data.Low, close=intraday_data.Close)])

# Display the chart.
fig.show()