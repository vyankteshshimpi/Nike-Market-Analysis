# ============================================================
# 01 - BRAND MOMENTUM ANALYSIS
# Nike vs Hoka vs On Running vs New Balance
# Data Source: Google Trends (via pytrends)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pytrends.request import TrendReq

# Create output folders if they don't already exist
os.makedirs('visualizations', exist_ok=True)
os.makedirs('data/raw', exist_ok=True)

print("Starting Brand Momentum Analysis...")

# ---- WHAT THIS DOES ----
# pytrends is a Python library that talks to Google Trends
# We connect to it here before making any requests
pytrends = TrendReq(hl='en-US', tz=360)

# The 4 brands we're comparing
brands = ['Nike', 'Hoka', 'On Running', 'New Balance']

# ---- WHAT THIS DOES ----
# We tell Google Trends: give us 5 years of worldwide search data
# for these 4 brands. The result is a score from 0-100 per week.
# 100 = peak popularity, 0 = barely searched.
pytrends.build_payload(brands, timeframe='today 5-y', geo='', gprop='')

print("Fetching data from Google Trends... (this may take 10-15 seconds)")
trends_df = pytrends.interest_over_time()

# Drop the 'isPartial' column — it just flags incomplete weeks, not useful
trends_df = trends_df.drop(columns=['isPartial'])

# Save the raw data so we don't have to re-fetch it later
trends_df.to_csv('data/raw/google_trends.csv')
print(f"Data saved. Shape: {trends_df.shape} ({trends_df.shape[0]} weeks of data)")
print(trends_df.tail(3))  # Show last 3 rows as a quick sanity check

# ============================================================
# CHART 1 — Brand Search Interest Over Time (Line Chart)
# ============================================================
# ---- WHAT THIS DOES ----
# Plots all 4 brands as lines over 5 years.
# If a brand's line goes up = growing consumer interest / mindshare.
# This is the "story" chart — it shows Nike's relative decline visually.

colors = {
    'Nike': '#111111',
    'Hoka': '#FF6B35',
    'On Running': '#00A3E0',
    'New Balance': '#CF142B'
}

sns.set_style("whitegrid")
plt.figure(figsize=(14, 7))

for brand in brands:
    plt.plot(trends_df.index, trends_df[brand],
             label=brand, color=colors[brand], linewidth=2.5)

plt.title("Brand Search Interest Over Time (2020–2025)\nNike vs. The Challengers",
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Search Interest (0–100)", fontsize=12)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('visualizations/01_brand_momentum.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 1 saved: visualizations/01_brand_momentum.png")

# ============================================================
# CHART 2 — Last 12 Months Average (Bar Chart Snapshot)
# ============================================================
# ---- WHAT THIS DOES ----
# Instead of over time, this shows WHERE EACH BRAND STANDS RIGHT NOW.
# We average the last 12 months of search data into a single number per brand.
# Higher bar = more consumer mindshare today.

recent_avg = trends_df.iloc[-52:].mean().sort_values(ascending=False)  # Last 52 weeks = ~12 months

plt.figure(figsize=(10, 6))
bars = plt.bar(recent_avg.index, recent_avg.values,
               color=[colors[b] for b in recent_avg.index],
               edgecolor='white', linewidth=0.5)

for bar, val in zip(bars, recent_avg.values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{val:.1f}', ha='center', fontweight='bold', fontsize=11)

plt.title("Average Search Interest — Last 12 Months\n(Higher = More Consumer Mindshare)",
          fontsize=14, fontweight='bold', pad=15)
plt.ylabel("Search Interest (0–100)", fontsize=12)
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig('visualizations/02_2024_snapshot.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 2 saved: visualizations/02_2024_snapshot.png")

# ============================================================
# SUMMARY — 5-Year Brand Momentum Change
# ============================================================
# ---- WHAT THIS DOES ----
# Compares the first 6 months of data vs the last 6 months.
# Tells us: is each brand growing or shrinking in public interest?

print("\n" + "="*50)
print("BRAND MOMENTUM SUMMARY (5-Year Change)")
print("="*50)

for brand in brands:
    early = trends_df.head(26)[brand].mean()   # First ~6 months
    recent = trends_df.tail(26)[brand].mean()  # Last ~6 months
    change = ((recent - early) / early) * 100
    direction = "UP" if change > 0 else "DOWN"
    print(f"  {direction:4s}  {brand}: {change:+.1f}% change in search interest")

print("\nDone! Check the visualizations/ folder for your charts.")
