import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def rsi(data, period=14):
  """Returns the RSI for the given data."""
  # Calculate the average up-moves.
  up_moves = data['Close'].diff()
  up_moves = up_moves.where(up_moves > 0, 0)
  up_mean = up_moves.rolling(period).mean()

  # Calculate the average down-moves.
  down_moves = data['Close'].diff()
  down_moves = down_moves.where(down_moves < 0, 0)
  down_mean = down_moves.abs().rolling(period).mean()

  # Calculate the RSI.
  rsi = 100 - (100 / (1 + up_mean / down_mean))

  return rsi

def enter_trade(data, rsi):
  """Returns True if we should enter a trade, False otherwise."""
  # Check if the RSI is below 30.
  if rsi< 30:
    return True
  else:
    return False


if __name__ == "__main__":
    # Download the intraday data for NKE for the past year with Data in interval of 1 Day.
    data = yf.download(tickers="NKE", period="1y", interval="1d", auto_adjust=True)
    rsi = rsi(data)
    print(rsi.index)
    #now choose Any of THe date you want to choose and pass it through the enter trade option.
    
    

      #  Plot the RSI.
    plt.plot(rsi)
    plt.axhline(30, color='red')
    plt.show()
