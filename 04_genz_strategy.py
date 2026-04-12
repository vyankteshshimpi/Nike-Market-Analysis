# ============================================================
# 04 - GENZ STRATEGY RECOMMENDATION
# "Nike Reborn" — A Data-Backed Product & GTM Strategy
# to reclaim cultural relevance with Generation Z
# ============================================================
# As the Nike Product Analytics team, we've identified the problem.
# Now we build the solution — backed by every data point we've collected.
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import seaborn as sns
import os

os.makedirs('visualizations', exist_ok=True)

print("Building GenZ Strategy Recommendation...")
print("="*55)

# ============================================================
# THE STRATEGIC INSIGHT — What our data told us
# ============================================================
# ---- WHAT THIS DOES ----
# Before we build charts, we summarize the key finding
# from each of our 3 previous analyses. This becomes
# the "The Gap" slide in our deck.

print("""
DATA SUMMARY — What We Found:

  Script 01 — Brand Momentum:
    Nike:        -2.0% search interest (5-year change)
    New Balance: +183.3% | Hoka: +160.8% | On Running: +138.5%

  Script 02 — Revenue:
    Nike is the ONLY brand shrinking (-10% YoY in 2025)
    On Running grew +147% | New Balance +112%

  Script 03 — Consumer Sentiment:
    Nike score: -0.372 (only negative brand)
    Top pain point: "GenZ sees it as their parents brand" (vol: 92)
    Second pain point: "Too expensive for quality drop" (vol: 90)

  CONCLUSION:
    Nike didn't lose on product alone — they lost on CULTURE.
    GenZ doesn't buy shoes. They buy identity.
    Nike's identity is stuck in the past.
""")

# ============================================================
# CHART 7 — Brand Positioning Map (The Whitespace)
# ============================================================
# ---- WHAT THIS DOES ----
# A 2x2 scatter plot mapping each brand on two axes:
#   X-axis: Cultural Authenticity (do consumers trust the brand feels real?)
#   Y-axis: GenZ Relevance (are young consumers actually buying/talking about it?)
# The EMPTY space on the chart = opportunity Nike can own.
# This is how product strategists identify "whitespace."

# Brand positions based on our data (scored 0-10 on each axis)
brands = {
    'Nike':        {'authenticity': 2.5, 'genz_relevance': 2.0,  'revenue': 46.3, 'color': '#111111'},
    'New Balance': {'authenticity': 8.5, 'genz_relevance': 8.0,  'revenue': 7.0,  'color': '#CF142B'},
    'Hoka':        {'authenticity': 7.0, 'genz_relevance': 5.5,  'revenue': 5.0,  'color': '#FF6B35'},
    'On Running':  {'authenticity': 7.5, 'genz_relevance': 6.5,  'revenue': 3.0,  'color': '#00A3E0'},
    'Nike\n(Target)': {'authenticity': 7.0, 'genz_relevance': 7.5, 'revenue': 50.0, 'color': '#555555'},
}

fig, ax = plt.subplots(figsize=(12, 9))

# Draw quadrant background shading
ax.axhspan(5, 10, xmin=0.5, xmax=1.0, alpha=0.06, color='green')   # Top-right = ideal
ax.axhspan(0, 5,  xmin=0.0, xmax=0.5, alpha=0.06, color='red')     # Bottom-left = danger zone

# Plot each brand as a bubble (size = revenue)
for brand, data in brands.items():
    size = data['revenue'] * 25  # Bubble size proportional to revenue
    alpha = 0.5 if 'Target' in brand else 0.85
    style = '--' if 'Target' in brand else '-'

    ax.scatter(data['authenticity'], data['genz_relevance'],
               s=size, color=data['color'], alpha=alpha,
               edgecolors='white', linewidth=2, zorder=5)

    # Label each bubble
    offset_x = 0.3
    offset_y = 0.3
    if 'Target' in brand:
        offset_x = 0.4
        ax.annotate('Nike\n(Where We\nNeed to Be)',
                    xy=(data['authenticity'], data['genz_relevance']),
                    xytext=(data['authenticity'] + offset_x, data['genz_relevance'] + offset_y),
                    fontsize=9, color='#555555', fontstyle='italic',
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))
    else:
        ax.annotate(brand,
                    xy=(data['authenticity'], data['genz_relevance']),
                    xytext=(data['authenticity'] + offset_x, data['genz_relevance'] + offset_y),
                    fontsize=11, fontweight='bold', color=data['color'])

# Draw arrow showing Nike's needed journey
ax.annotate('',
            xy=(6.8, 7.3),       # Target position
            xytext=(2.9, 2.4),   # Current Nike position
            arrowprops=dict(arrowstyle='->', color='#555555',
                            lw=2.5, linestyle='dashed',
                            connectionstyle='arc3,rad=0.2'))

# Axis labels and quadrant text
ax.set_xlabel("Cultural Authenticity →\n(Do consumers see this brand as real and trustworthy?)",
              fontsize=12, labelpad=10)
ax.set_ylabel("GenZ Relevance →\n(Are Gen Z consumers buying and talking about this brand?)",
              fontsize=12, labelpad=10)
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
ax.axvline(x=5, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
ax.axhline(y=5, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)

# Quadrant labels
ax.text(7.5, 9.5, "WIN ZONE\n(Authentic + Relevant)", fontsize=9, color='green',
        alpha=0.6, ha='center', fontweight='bold')
ax.text(2.5, 1.0, "DANGER ZONE\n(Corporate + Irrelevant)", fontsize=9, color='red',
        alpha=0.6, ha='center', fontweight='bold')

# Bubble size legend
for rev, label in [(3.0, '$3B'), (7.0, '$7B'), (46.3, '$46B')]:
    ax.scatter([], [], s=rev * 25, color='gray', alpha=0.5, label=f'{label} revenue')
ax.legend(title="Bubble size = Revenue", loc='upper left', fontsize=9)

ax.set_title("Brand Positioning Map: Cultural Authenticity vs. GenZ Relevance\n"
             "Nike needs to move from Danger Zone → Win Zone",
             fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('visualizations/07_brand_positioning_map.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 7 saved: visualizations/07_brand_positioning_map.png")

# ============================================================
# CHART 8 — The "Nike Reborn" Strategy Framework
# ============================================================
# ---- WHAT THIS DOES ----
# A visual summary of our 3-pillar strategy recommendation.
# Each pillar addresses one of Nike's top pain points from our data.
# This becomes Slide 8 in the deck — the strategy slide.

fig, axes = plt.subplots(1, 3, figsize=(16, 8))
fig.patch.set_facecolor('#0a0a0a')  # Dark background for impact

pillars = [
    {
        'title': 'PILLAR 1\nCommunity-First\nDrops',
        'problem': 'Pain Point: Availability score -1.00\n"Bots & resellers killed the culture"',
        'solution': '→ Verified local buyer program\n→ In-store community access\n→ Anti-bot authentication\n→ 60% of drops reserved for\n   real Nike community members',
        'kpi': 'KPI: Community drop sell-through\nTarget: 80% to verified locals',
        'color': '#1a1a2e',
        'accent': '#e94560'
    },
    {
        'title': 'PILLAR 2\nGenZ\nCo-Creation',
        'problem': 'Pain Point: GenZ Appeal score -0.51\n"Nike feels like my parents brand"',
        'solution': '→ Nike Design Lab platform\n→ GenZ designers submit concepts\n→ Community votes on top designs\n→ Winners get produced & credited\n→ 12 community drops per year',
        'kpi': 'KPI: Platform submissions & votes\nTarget: 500K GenZ designers by Y2',
        'color': '#16213e',
        'accent': '#0f3460'
    },
    {
        'title': 'PILLAR 3\nCultural\nPartnerships',
        'problem': 'Pain Point: Brand Identity score -0.23\n"Feels corporate, lost its cool"',
        'solution': '→ Partner with underground artists\n   NOT mainstream celebrities\n→ Sponsor local sports culture:\n   street football, skate, dance\n→ Pull back from mass advertising\n→ Let the product speak first',
        'kpi': 'KPI: Earned media & UGC volume\nTarget: 40% increase in organic posts',
        'color': '#0f3460',
        'accent': '#533483'
    }
]

for ax, pillar in zip(axes, pillars):
    ax.set_facecolor(pillar['color'])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Pillar title
    ax.text(0.5, 0.90, pillar['title'], ha='center', va='top',
            fontsize=14, fontweight='bold', color='white',
            transform=ax.transAxes, linespacing=1.4)

    # Accent line
    ax.add_patch(mpatches.FancyBboxPatch((0.1, 0.72), 0.8, 0.03,
                 boxstyle="round,pad=0", color=pillar['accent'],
                 transform=ax.transAxes))

    # Problem being solved
    ax.text(0.5, 0.68, pillar['problem'], ha='center', va='top',
            fontsize=8.5, color='#aaaaaa', fontstyle='italic',
            transform=ax.transAxes, linespacing=1.5)

    # Solution bullets
    ax.text(0.5, 0.52, pillar['solution'], ha='center', va='top',
            fontsize=9.5, color='white',
            transform=ax.transAxes, linespacing=1.6)

    # KPI box
    ax.add_patch(mpatches.FancyBboxPatch((0.05, 0.05), 0.9, 0.13,
                 boxstyle="round,pad=0.02", color=pillar['accent'],
                 alpha=0.4, transform=ax.transAxes))
    ax.text(0.5, 0.115, pillar['kpi'], ha='center', va='center',
            fontsize=8.5, color='white', fontweight='bold',
            transform=ax.transAxes, linespacing=1.5)

fig.suptitle('"NIKE REBORN" — A 3-Pillar GenZ Strategy\nData-Driven. Culture-First. Community-Led.',
             fontsize=16, fontweight='bold', color='white', y=1.01)

plt.tight_layout()
plt.savefig('visualizations/08_strategy_framework.png', dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.show()
print("Chart 8 saved: visualizations/08_strategy_framework.png")

# ============================================================
# CHART 9 — Expected Impact (KPI Projections)
# ============================================================
# ---- WHAT THIS DOES ----
# Shows what we expect to happen to Nike's key metrics
# if they execute the strategy over 3 years.
# This turns our strategy into a business case.

years = ['2025\n(Now)', '2026\n(Year 1)', '2027\n(Year 2)', '2028\n(Year 3)']

metrics = {
    'GenZ Search Interest\n(Index Score)': {
        'values': [30, 42, 58, 72],
        'color': '#e94560',
        'target': 75,
        'unit': ''
    },
    'Consumer Sentiment\nScore (-1 to +1)': {
        'values': [-0.37, 0.05, 0.25, 0.45],
        'color': '#00A3E0',
        'target': 0.50,
        'unit': ''
    },
    'Revenue Growth\nRate (%)': {
        'values': [-10, 2, 8, 15],
        'color': '#4CAF50',
        'target': 15,
        'unit': '%'
    }
}

fig, axes = plt.subplots(1, 3, figsize=(16, 6))
sns.set_style("whitegrid")

for ax, (metric, data) in zip(axes, metrics.items()):
    ax.plot(years, data['values'], color=data['color'],
            linewidth=3, marker='o', markersize=9, zorder=5)

    # Shade area under the line
    ax.fill_between(range(len(years)), data['values'],
                    alpha=0.12, color=data['color'])

    # Add value labels
    for i, val in enumerate(data['values']):
        label = f"+{val}{data['unit']}" if val > 0 else f"{val}{data['unit']}"
        ax.annotate(label, (i, val),
                    textcoords="offset points", xytext=(0, 12),
                    ha='center', fontweight='bold', fontsize=10,
                    color=data['color'])

    # Reference line at 0 for metrics that have positive/negative
    if min(data['values']) < 0:
        ax.axhline(y=0, color='gray', linewidth=1, linestyle='--', alpha=0.6)

    ax.set_title(metric, fontsize=12, fontweight='bold', pad=12)
    ax.set_xticks(range(len(years)))
    ax.set_xticklabels(years, fontsize=9)
    ax.tick_params(axis='y', labelsize=9)

fig.suptitle('"Nike Reborn" — Projected Impact Over 3 Years\n(If Strategy Executed Fully)',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('visualizations/09_projected_impact.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 9 saved: visualizations/09_projected_impact.png")

# ============================================================
# FINAL SUMMARY PRINT
# ============================================================
print("\n" + "="*55)
print("NIKE REBORN — STRATEGY SUMMARY")
print("="*55)
print("""
  THE PROBLEM (Data-Backed):
    • Nike is the only brand shrinking (-10% revenue YoY)
    • Only brand with negative consumer sentiment (-0.372)
    • GenZ sees Nike as "their parents brand" — #1 pain point
    • Lost casual to New Balance, performance to Hoka/On Running

  THE STRATEGY — 3 Pillars:
    1. Community-First Drops
       Fix the bot/reseller problem. Give real fans first access.

    2. GenZ Co-Creation Platform
       Let GenZ design the shoes. Make Nike a canvas, not a brand.

    3. Underground Cultural Partnerships
       Stop sponsoring superstars. Start funding street culture.

  THE TARGET (3-Year Goals):
    • GenZ Search Index: 30 → 72 (+140%)
    • Consumer Sentiment: -0.37 → +0.45 (flip to positive)
    • Revenue Growth Rate: -10% → +15% (return to growth)

  CORE INSIGHT:
    GenZ doesn't buy shoes. They buy identity.
    Nike needs to stop selling shoes and start
    building a community GenZ actually wants to belong to.
""")
print("All 9 charts saved. Project analysis complete!")
print("Check your visualizations/ folder.")
