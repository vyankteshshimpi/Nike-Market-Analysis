import pandas as pd

df = pd.read_csv("data/levis_quarterly_financials.csv", index_col=0)

revenue = df["Total Revenue"].dropna()
revenue = revenue.sort_index()
print(revenue)

growth = revenue.pct_change()
print(growth)