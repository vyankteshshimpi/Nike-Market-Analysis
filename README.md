# Nike Market Analysis — Sole Survivor?

> *"Nike doesn't need a new shoe. It needs a new relationship with the next generation."*

## Project Overview

A full data-driven market analysis of the global athletic footwear industry — investigating why Nike is losing ground to challenger brands like New Balance, Hoka, and On Running, and building a product strategy to win back Generation Z.

Built as a portfolio project from the perspective of a **Nike Product Analytics Team**.

---

## The Core Finding

Nike didn't lose on product — it lost on **culture**.

GenZ stopped seeing Nike as their brand. New Balance became the cool casual shoe. Hoka owns serious running. On Running owns the premium space. Nike got left with nostalgia — and GenZ doesn't buy nostalgia. They buy identity.

---

## Key Data Findings

| Metric | Nike | New Balance | Hoka | On Running |
|--------|------|-------------|------|------------|
| 5yr Search Interest Change | -2% | +183% | +160% | +138% |
| Revenue Growth (Total) | -1% | +112% | +58% | +147% |
| Consumer Sentiment Score | -0.372 | +0.833 | +0.403 | +0.486 |

---

## Analysis Techniques

| Script | Technique | Data Source |
|--------|-----------|-------------|
| `01_brand_momentum.py` | Time-series trend analysis | Google Trends (pytrends) |
| `02_revenue_analysis.py` | Financial benchmarking | Yahoo Finance (yfinance) |
| `03_consumer_sentiment.py` | NLP sentiment scoring | Reddit, Amazon Reviews |
| `04_genz_strategy.py` | Whitespace mapping & KPI projection | Derived from above |

---

## The Strategy — "Nike Reborn"

Three data-backed pillars to reclaim GenZ:

**Pillar 1 — Community-First Drops**
Fix the bot/reseller problem. Reserve 60% of drops for verified real fans.
KPI: 80% community drop sell-through

**Pillar 2 — GenZ Co-Creation**
Launch Nike Design Lab — let GenZ designers submit concepts, community votes, winners get produced.
KPI: 500K GenZ designers on platform by Year 2

**Pillar 3 — Cultural Partnerships**
Partner with underground artists and local street culture — not superstars.
KPI: 40% increase in organic social posts

---

## Projected 3-Year Impact

| KPI | Now (2025) | Year 3 Target |
|-----|------------|---------------|
| GenZ Search Index | 30 | 72 (+140%) |
| Consumer Sentiment | -0.37 | +0.45 |
| Revenue Growth Rate | -10% | +15% |

---

## Tools & Libraries

- Python, Pandas, Matplotlib, Seaborn
- pytrends (Google Trends API)
- yfinance (Yahoo Finance)
- python-pptx (PowerPoint generation)

---

## Files

Nike_Market_Analysis/
├── 01_brand_momentum.py
├── 02_revenue_analysis.py
├── 03_consumer_sentiment.py
├── 04_genz_strategy.py
├── Nike_Market_Analysis_Deck.pptx
├── data/
│ ├── raw/
│ └── processed/
└── visualizations/
├── 01_brand_momentum.png
├── 02_2024_snapshot.png
├── 03_revenue_trends.png
├── 04_revenue_growth_rate.png
├── 05_sentiment_scores.png
├── 06_sentiment_heatmap.png
├── 07_brand_positioning_map.png
├── 08_strategy_framework.png
└── 09_projected_impact.png


---

*Built by Vyanktesh Shimpi | MS Business Analytics & AI, UT Dallas*

