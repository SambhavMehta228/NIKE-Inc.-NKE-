The code here first imports the yfinance, pandas, and plotly libraries. These libraries are used to download, analyze, and visualize financial data.

Next, the code downloads intraday data for NIKE, Inc. (NKE) for the past year with data in interval of 1 Day. The yf.download() function is used to download the data. The tickers parameter specifies the ticker symbol of the stock, the period parameter specifies the time period for the data, the interval parameter specifies the interval of the data, and the auto_adjust parameter specifies whether to automatically adjust the data for splits and dividends.

The code then prints the data type of the downloaded data, the first rows of the data, the column names of the data, information about the data, the maximum and minimum dates in the data, and the average daily trading volume.

Finally, the code creates a candlestick chart of the data. A candlestick chart is a type of chart that is used to visualize the price movements of a security. The go.Figure() function is used to create the chart, and the go.Candlestick() function is used to add the candlesticks to the chart.

The CHallenges I faced during making of this assignment were, Finding correct tools to find Historical Data of a publicly traded company and Visualise that Data .  

The code also displays the chart.
