# ============================================================
# 02 - REVENUE & FINANCIAL PERFORMANCE ANALYSIS
# Nike vs On Running vs Deckers (Hoka parent) vs New Balance
# Data Source: yfinance (real stock market financial data)
#              + manually entered New Balance estimates (private company)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import yfinance as yf
import os

os.makedirs('visualizations', exist_ok=True)
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

print("Starting Revenue & Financial Analysis...")

# ============================================================
# STEP 1 — PULL REVENUE DATA FROM YAHOO FINANCE
# ============================================================
# ---- WHAT THIS DOES ----
# yfinance lets us download real financial data for any public company.
# NKE = Nike, ONON = On Running, DECK = Deckers Outdoor (owns Hoka)
# We pull their annual income statements which include total revenue.

tickers = {
    'Nike': 'NKE',
    'On Running': 'ONON',
    'Deckers (Hoka)': 'DECK'
}

revenue_data = {}

for brand, ticker in tickers.items():
    print(f"  Fetching {brand} ({ticker})...")
    stock = yf.Ticker(ticker)

    # ---- WHAT THIS DOES ----
    # .financials gives us the annual income statement.
    # We look for the 'Total Revenue' row and convert from dollars to billions.
    financials = stock.financials

    if 'Total Revenue' in financials.index:
        rev = financials.loc['Total Revenue'] / 1e9  # Convert to billions
        revenue_data[brand] = rev.sort_index()  # Sort oldest to newest

print("  Data fetched successfully!")

# ---- WHAT THIS DOES ----
# New Balance is a private company — they don't publish on stock markets.
# We use publicly reported revenue estimates from news and industry sources.
# Sources: Forbes, Statista, company press releases
new_balance_revenue = pd.Series({
    pd.Timestamp('2020-12-31'): 3.3,
    pd.Timestamp('2021-12-31'): 4.0,
    pd.Timestamp('2022-12-31'): 5.1,
    pd.Timestamp('2023-12-31'): 6.5,
    pd.Timestamp('2024-12-31'): 7.0,   # Estimate
})
revenue_data['New Balance'] = new_balance_revenue

# Save processed data
all_revenue = pd.DataFrame(revenue_data)
all_revenue.to_csv('data/processed/revenue_data.csv')
print("  Revenue data saved to data/processed/revenue_data.csv")

# Print a quick summary
print("\nRevenue Snapshot (most recent year, in $Billions):")
for brand in revenue_data:
    latest = revenue_data[brand].dropna().iloc[-1]
    year = revenue_data[brand].dropna().index[-1].year
    print(f"  {brand}: ${latest:.1f}B ({year})")

# ============================================================
# CHART 3 — Revenue Over Time (Line Chart)
# ============================================================
# ---- WHAT THIS DOES ----
# Shows how each brand's annual revenue has changed over time.
# Nike is a giant — but look at the SLOPE of the challengers.
# A steep upward slope = fast growth even if the number is smaller.

colors = {
    'Nike': '#111111',
    'On Running': '#00A3E0',
    'Deckers (Hoka)': '#FF6B35',
    'New Balance': '#CF142B'
}

sns.set_style("whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# --- Left chart: All brands together (absolute revenue) ---
ax1 = axes[0]
for brand, rev in revenue_data.items():
    rev_clean = rev.dropna()
    ax1.plot(rev_clean.index.year, rev_clean.values,
             label=brand, color=colors[brand], linewidth=2.5, marker='o', markersize=5)

ax1.set_title("Annual Revenue — All Brands\n(Absolute $Billions)", fontsize=13, fontweight='bold')
ax1.set_xlabel("Year")
ax1.set_ylabel("Revenue ($B)")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.0f}B'))
ax1.legend()

# --- Right chart: Challengers only (zoom in, no Nike) ---
# ---- WHAT THIS DOES ----
# Nike's size makes challengers look flat.
# By removing Nike, we see how fast Hoka, On Running, New Balance are actually growing.
ax2 = axes[1]
challengers = ['On Running', 'Deckers (Hoka)', 'New Balance']
for brand in challengers:
    rev_clean = revenue_data[brand].dropna()
    ax2.plot(rev_clean.index.year, rev_clean.values,
             label=brand, color=colors[brand], linewidth=2.5, marker='o', markersize=5)

ax2.set_title("Challenger Brands Revenue Growth\n(Zoom-In, Nike Removed)", fontsize=13, fontweight='bold')
ax2.set_xlabel("Year")
ax2.set_ylabel("Revenue ($B)")
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.1f}B'))
ax2.legend()

plt.suptitle("Revenue Trends: Nike vs. The Challengers", fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('visualizations/03_revenue_trends.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 3 saved: visualizations/03_revenue_trends.png")

# ============================================================
# CHART 4 — Revenue Growth Rate (% Change Year-over-Year)
# ============================================================
# ---- WHAT THIS DOES ----
# Instead of raw dollars, this shows GROWTH RATE — how fast is each brand growing?
# A small brand growing 30% year-over-year is far more threatening
# than a giant growing 2%. This is the key strategic insight.

fig, ax = plt.subplots(figsize=(12, 6))

for brand, rev in revenue_data.items():
    rev_clean = rev.dropna().sort_index()
    growth = rev_clean.pct_change() * 100  # Convert to percentage
    growth = growth.dropna()
    ax.plot(growth.index.year, growth.values,
            label=brand, color=colors[brand], linewidth=2.5, marker='o', markersize=5)

# Add a reference line at 0% — below = shrinking, above = growing
ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7)

ax.set_title("Year-Over-Year Revenue Growth Rate (%)\nWho Is Growing Fastest?",
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Revenue Growth (%)", fontsize=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}%'))
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('visualizations/04_revenue_growth_rate.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 4 saved: visualizations/04_revenue_growth_rate.png")

# ============================================================
# SUMMARY — Revenue Growth Stats
# ============================================================
print("\n" + "="*50)
print("REVENUE GROWTH SUMMARY")
print("="*50)
for brand, rev in revenue_data.items():
    rev_clean = rev.dropna().sort_index()
    if len(rev_clean) >= 2:
        start = rev_clean.iloc[0]
        end = rev_clean.iloc[-1]
        total_growth = ((end - start) / start) * 100
        print(f"  {brand}: ${start:.1f}B → ${end:.1f}B  ({total_growth:+.0f}% total growth)")

print("\nDone! Check visualizations/ folder for Charts 3 & 4.")
