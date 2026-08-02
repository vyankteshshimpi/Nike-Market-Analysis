def project_profit(base, growth_rate, quarters):
    profit = base
    for i in range(quarters):
        profit = profit + (profit * growth_rate)
    return profit

total_investment = 50_000_000

womens_denim_growth_rate = 0.08
asia_expansion_growth_rate = 0.05

splits = [0.5, 0.6, 0.7]

for split in splits:
    womens_investment = total_investment * split
    asia_investment = total_investment * (1 - split)

    womens_result = project_profit(womens_investment, womens_denim_growth_rate, 6)
    asia_result = project_profit(asia_investment, asia_expansion_growth_rate, 6)

    total_result = womens_result + asia_result

    print(f"Split: {int(split*100)}% Women's Denim / {int((1-split)*100)}% Asia Expansion")
    print(f"  Women's Denim: ${womens_investment:,.0f} -> ${womens_result:,.0f}")
    print(f"  Asia Expansion: ${asia_investment:,.0f} -> ${asia_result:,.0f}")
    print(f"  Total after 6 quarters: ${total_result:,.0f}")
    print()