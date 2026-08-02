import yfinance as yf
import pandas as pd

levi = yf.Ticker("LEVI")
financials = levi.quarterly_financials.T

print(financials.head())

financials.to_csv("data/levis_quarterly_financials.csv")
print(financials.shape)
print(financials.columns)
print(financials["Total Revenue"])