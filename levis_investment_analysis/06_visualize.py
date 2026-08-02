import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("visualizations", exist_ok=True)

colors = ["#2a78d6", "#eb6834", "#1baf7a"]

# Chart 1: Product line trend comparison
product_trends = pd.read_csv("data/product_line_trends.csv", index_col=0, parse_dates=True)

plt.figure(figsize=(10, 5))
plt.plot(product_trends.index, product_trends["women's denim"], label="Women's Denim", color=colors[0], linewidth=2)
plt.plot(product_trends.index, product_trends["sustainable denim"], label="Sustainable Denim", color=colors[1], linewidth=2)
plt.plot(product_trends.index, product_trends["athleisure jeans"], label="Athleisure Jeans", color=colors[2], linewidth=2)
plt.title("Product Line Search Interest Over 5 Years")
plt.xlabel("Date")
plt.ylabel("Search Interest (0-100)")
plt.legend()
plt.savefig("visualizations/01_product_line_trends.png")
plt.close()
print("Saved chart 1: product line trends")

# Chart 2: China vs India trend comparison
asia_trends = pd.read_csv("data/asia_market_trends.csv", index_col=0, parse_dates=True)

plt.figure(figsize=(10, 5))
plt.plot(asia_trends.index, asia_trends["Levi's China"], label="China", color=colors[0], linewidth=2)
plt.plot(asia_trends.index, asia_trends["Levi's India"], label="India", color=colors[1], linewidth=2)
plt.title("China vs. India Search Interest Over 5 Years")
plt.xlabel("Date")
plt.ylabel("Search Interest (0-100)")
plt.legend()
plt.savefig("visualizations/02_asia_market_trends.png")
plt.close()
print("Saved chart 2: Asia market trends")

# Chart 3: Profit projection by allocation split
def project_profit(base, growth_rate, quarters):
    profit = base
    for i in range(quarters):
        profit = profit + (profit * growth_rate)
    return profit

total_investment = 50_000_000
womens_denim_growth_rate = 0.08
asia_expansion_growth_rate = 0.05
splits = [0.5, 0.6, 0.7]

labels = []
totals = []
for split in splits:
    womens_result = project_profit(total_investment * split, womens_denim_growth_rate, 6)
    asia_result = project_profit(total_investment * (1 - split), asia_expansion_growth_rate, 6)
    labels.append(f"{int(split*100)}/{int((1-split)*100)}")
    totals.append(womens_result + asia_result)

plt.figure(figsize=(8, 5))
plt.bar(labels, totals, color=colors[0])
plt.title("Projected Total Value After 6 Quarters by Allocation Split")
plt.xlabel("Women's Denim / Asia Expansion Split")
plt.ylabel("Total Value ($)")
plt.savefig("visualizations/03_profit_projection.png")
plt.close()
print("Saved chart 3: profit projection")