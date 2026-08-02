from pytrends.request import TrendReq
import pandas as pd

pd.set_option('display.width', 120)
pd.set_option('display.max_columns', None)

pytrends = TrendReq(hl='en-US', tz=360)

keywords = ["sustainable denim", "athleisure jeans", "women's denim"]
pytrends.build_payload(keywords, timeframe='today 5-y', geo='', gprop='')

trends_df = pytrends.interest_over_time()
trends_df = trends_df.drop(columns=['isPartial'])

trends_df.to_csv("data/product_line_trends.csv")

recent = trends_df.tail(52).mean()
early = trends_df.head(52).mean()
momentum_change = ((recent - early) / early) * 100

print("Average interest - most recent year:")
print(recent)
print("\n% change in search interest over 5 years (momentum score):")
print(momentum_change)