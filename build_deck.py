"""
Nike Market Analysis Deck Builder
Replicates the Google Slides "Consulting Proposal" dark-navy template style.
Run:  python build_deck.py
Output: Nike_Market_Analysis_Deck.pptx (same directory)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ---------------------------------------------------------------------------
# COLOUR CONSTANTS
# ---------------------------------------------------------------------------
BG     = RGBColor(0x1C, 0x22, 0x33)   # dark navy - all slide backgrounds
BLUE   = RGBColor(0x2E, 0x50, 0xD6)   # blue parallelogram
MINT   = RGBColor(0x7D, 0xC4, 0xB4)   # mint/sage parallelogram
PURPLE = RGBColor(0x78, 0x78, 0xC8)   # accent
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
BODY   = RGBColor(0xCC, 0xCC, 0xCC)   # body text
MUTED  = RGBColor(0x88, 0x88, 0x88)   # captions
BORDER = RGBColor(0x2E, 0x3A, 0x50)   # thin box border
BOX_BG = RGBColor(0x22, 0x2B, 0x3D)   # content box background

# ---------------------------------------------------------------------------
# SLIDE DIMENSIONS — LAYOUT_WIDE = 13.33" x 7.5"
# ---------------------------------------------------------------------------
SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

VIZ = "/Users/vyankteshshimpi/Downloads/projects/Nike_Market_Analysis/visualizations"


# ---------------------------------------------------------------------------
# HELPER: apply font props to a run
# ---------------------------------------------------------------------------
def run_font(run, name="Calibri", size_pt=None, bold=None, italic=None, color=None):
    run.font.name = name
    if size_pt:
        run.font.size = Pt(size_pt)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    if color:
        run.font.color.rgb = color


# ---------------------------------------------------------------------------
# HELPER: add a simple text box
# ---------------------------------------------------------------------------
def add_text(slide, text, x, y, w, h,
             font="Calibri", size=13, color=BODY,
             bold=False, italic=False, align=PP_ALIGN.LEFT):
    txBox = slide.shapes.add_textbox(
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run_font(run, font, size, bold, italic, color)
    return txBox


# ---------------------------------------------------------------------------
# HELPER: add a rectangle content box (optionally with top accent border)
# ---------------------------------------------------------------------------
def add_box(slide, x, y, w, h,
            bg_color=BOX_BG, border_color=BORDER, border_pt=1,
            top_border_color=None, top_border_pt=3):
    shape = slide.shapes.add_shape(
        1,  # RECTANGLE
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(border_pt)

    if top_border_color:
        # Draw a thin accent strip across the top
        strip_h = top_border_pt / 72.0  # pts to inches
        accent = slide.shapes.add_shape(
            1,
            Inches(x), Inches(y), Inches(w), Inches(strip_h)
        )
        accent.fill.solid()
        accent.fill.fore_color.rgb = top_border_color
        accent.line.fill.background()

    return shape


# ---------------------------------------------------------------------------
# HELPER: add a parallelogram
# ---------------------------------------------------------------------------
def add_parallelogram(slide, x, y, w, h, rotation, color):
    shape = slide.shapes.add_shape(
        2,  # PARALLELOGRAM
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.rotation = rotation
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


# ---------------------------------------------------------------------------
# HELPER: signature top-left corner decoration (every slide)
# ---------------------------------------------------------------------------
def add_corner_decoration(slide):
    # Blue (behind) - larger
    add_parallelogram(slide, x=-0.3, y=-0.5, w=2.2, h=4.0,
                      rotation=-30, color=BLUE)
    # Mint (front) - smaller
    add_parallelogram(slide, x=0.2, y=-0.3, w=1.8, h=3.2,
                      rotation=-30, color=MINT)


# ---------------------------------------------------------------------------
# HELPER: set dark navy background
# ---------------------------------------------------------------------------
def set_bg(slide):
    bg = slide.shapes.add_shape(
        1, Emu(0), Emu(0), SLIDE_W, SLIDE_H
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    bg.line.fill.background()
    # Push to back of z-order (index 2 is after the sp tree header)
    slide.shapes._spTree.remove(bg._element)
    slide.shapes._spTree.insert(2, bg._element)


# ---------------------------------------------------------------------------
# HELPER: slide title
# ---------------------------------------------------------------------------
def add_title(slide, text, x=2.5, y=0.5, w=10.0, size=34):
    return add_text(slide, text, x=x, y=y, w=w, h=0.7,
                    font="Calibri", size=size, color=WHITE, bold=False)


# ===========================================================================
# SLIDE 1 - TITLE
# ===========================================================================
def build_slide1(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    # Right-side decorative parallelograms
    add_parallelogram(slide, x=11.0, y=2.8, w=1.5, h=2.8, rotation=-30, color=MINT)
    add_parallelogram(slide, x=11.6, y=3.5, w=1.2, h=2.2, rotation=-30, color=BLUE)

    add_text(slide, "Sole Survivor?",
             x=4.5, y=2.8, w=8.0, h=1.1,
             font="Calibri", size=56, color=WHITE)

    add_text(slide,
             "A Data-Driven Analysis of Nike's Market Position\n"
             "and a Strategy to Reclaim Generation Z",
             x=4.5, y=4.1, w=8.0, h=1.0,
             font="Calibri", size=16, color=BODY)

    add_text(slide, "Nike Product Analytics Team  \u00b7  April 2025",
             x=4.5, y=6.5, w=8.0, h=0.4,
             font="Calibri", size=12, color=MUTED)


# ===========================================================================
# SLIDE 2 - THE SHIFT
# ===========================================================================
def build_slide2(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "The Ground Is Shifting Under Nike's Feet",
              x=2.5, y=0.5, w=10.5, size=36)

    # Stat boxes
    stats = [
        (0.4,  "-2%",        "Nike 5yr search interest",  MINT,   48),
        (4.57, "+138\u2013183%", "Challenger brand growth", MINT, 36),
        (8.73, "-10%",        "Nike revenue growth 2025",  PURPLE, 48),
    ]
    for bx, num, lbl, col, sz in stats:
        add_box(slide, x=bx, y=1.6, w=4.0, h=1.5)
        add_text(slide, num,
                 x=bx+0.15, y=1.65, w=3.7, h=0.85,
                 font="Calibri", size=sz, color=col, bold=True)
        add_text(slide, lbl,
                 x=bx+0.15, y=2.6, w=3.7, h=0.4,
                 font="Calibri", size=12, color=MUTED)

    # Summary line
    add_text(slide,
             "For the first time in decades, Nike is the only major athletic brand that is shrinking.",
             x=0.4, y=3.3, w=12.7, h=0.35,
             font="Calibri", size=13, color=MUTED, italic=True)

    # Chart image
    slide.shapes.add_picture(
        os.path.join(VIZ, "01_brand_momentum.png"),
        Inches(0.4), Inches(3.7), Inches(12.5), Inches(3.4)
    )


# ===========================================================================
# SLIDE 3 - MARKET LANDSCAPE
# ===========================================================================
def build_slide3(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "The Global Athletic Footwear Market",
              x=2.5, y=0.5, w=10.0, size=34)

    # Left content box
    add_box(slide, x=0.4, y=1.3, w=6.0, h=3.5)

    facts = [
        "Global market: $115B in 2024  \u2192  projected $200B by 2030",
        "Nike market share: ~27% \u2014 down from 35% in 2019",
        "Fastest growing: Performance Running & Lifestyle",
        "Key challengers: New Balance, Hoka, On Running, Adidas",
    ]
    for i, fact in enumerate(facts):
        fy = 1.42 + i * 0.78
        # mint square bullet
        sq = slide.shapes.add_shape(1, Inches(0.57), Inches(fy + 0.06),
                                    Inches(0.12), Inches(0.12))
        sq.fill.solid()
        sq.fill.fore_color.rgb = MINT
        sq.line.fill.background()
        add_text(slide, fact, x=0.78, y=fy, w=5.45, h=0.68,
                 font="Calibri", size=13, color=BODY)

    # Purple insight card
    card = slide.shapes.add_shape(
        1, Inches(0.4), Inches(4.97), Inches(6.0), Inches(0.65)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = PURPLE
    card.line.fill.background()
    add_text(slide,
             "Nike\u2019s share of a GROWING market is falling \u2014 a compounding crisis.",
             x=0.55, y=4.99, w=5.7, h=0.6,
             font="Calibri", size=13, color=WHITE, italic=True)

    # Right image
    slide.shapes.add_picture(
        os.path.join(VIZ, "02_2024_snapshot.png"),
        Inches(6.7), Inches(1.2), Inches(6.2), Inches(5.9)
    )


# ===========================================================================
# SLIDE 4 - THE CHALLENGERS
# ===========================================================================
def build_slide4(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "Meet the Brands Eating Nike's Lunch",
              x=2.5, y=0.5, w=10.0, size=34)

    cards = [
        (0.35,  MINT,   MINT,   "NEW BALANCE",  "+183%", "$3.3B \u2192 $7.0B", MINT,   "Owns the GenZ casual space"),
        (4.67,  BLUE,   PURPLE, "HOKA",         "+160%", "$3.2B \u2192 $5.0B", PURPLE, "Owns performance running"),
        (8.98,  PURPLE, PURPLE, "ON RUNNING",   "+138%", "$1.2B \u2192 $3.0B", PURPLE, "Owns premium aspirational"),
    ]

    for cx, top_color, brand_color, brand, pct, rev, rev_color, desc in cards:
        add_box(slide, x=cx, y=1.4, w=4.0, h=5.6,
                top_border_color=top_color, top_border_pt=3)

        add_text(slide, brand, x=cx+0.15, y=1.55, w=3.7, h=0.35,
                 font="Calibri", size=13, color=brand_color, bold=True)

        add_text(slide, pct, x=cx+0.15, y=1.95, w=3.7, h=0.95,
                 font="Calibri", size=44, color=WHITE, bold=True)

        add_text(slide, "search interest (5yr)", x=cx+0.15, y=2.95, w=3.7, h=0.3,
                 font="Calibri", size=11, color=MUTED)

        # divider
        d1 = slide.shapes.add_shape(1, Inches(cx+0.15), Inches(3.33),
                                    Inches(3.7), Inches(0.02))
        d1.fill.solid(); d1.fill.fore_color.rgb = BORDER
        d1.line.fill.background()

        add_text(slide, rev, x=cx+0.15, y=3.4, w=3.7, h=0.5,
                 font="Calibri", size=20, color=rev_color, bold=True)

        add_text(slide, "revenue", x=cx+0.15, y=3.93, w=3.7, h=0.3,
                 font="Calibri", size=11, color=MUTED)

        # divider
        d2 = slide.shapes.add_shape(1, Inches(cx+0.15), Inches(4.3),
                                    Inches(3.7), Inches(0.02))
        d2.fill.solid(); d2.fill.fore_color.rgb = BORDER
        d2.line.fill.background()

        add_text(slide, desc, x=cx+0.15, y=4.36, w=3.7, h=0.5,
                 font="Calibri", size=13, color=BODY, italic=True)

    add_text(slide,
             "All three grew revenue 58\u2013147% while Nike declined.",
             x=0.4, y=7.15, w=12.5, h=0.3,
             font="Calibri", size=11, color=MUTED)


# ===========================================================================
# SLIDE 5 - NIKE BY THE NUMBERS
# ===========================================================================
def build_slide5(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "Nike By The Numbers: A Brand in Decline",
              x=2.5, y=0.5, w=10.0, size=34)

    # Left content box
    add_box(slide, x=0.4, y=1.3, w=5.5, h=5.2)

    add_text(slide, "Revenue is shrinking.",
             x=0.6, y=1.42, w=5.1, h=0.4,
             font="Calibri", size=16, color=WHITE, bold=True)

    add_text(slide,
             "Nike posted -10% revenue growth in FY2025 \u2014 its steepest decline in over a "
             "decade. Every challenger brand grew 15\u201330% in the same period.",
             x=0.6, y=1.88, w=5.1, h=1.0,
             font="Calibri", size=13, color=BODY)

    add_text(slide, "Client Implications:",
             x=0.6, y=3.05, w=5.1, h=0.4,
             font="Calibri", size=14, color=WHITE, bold=True)

    for i, bullet in enumerate([
        "Nike is losing ground in its core markets",
        "Challengers are accelerating while Nike retreats"
    ]):
        add_text(slide, "\u00b7  " + bullet,
                 x=0.7, y=3.55 + i * 0.58, w=5.0, h=0.48,
                 font="Calibri", size=13, color=BODY)

    # Right chart
    slide.shapes.add_picture(
        os.path.join(VIZ, "04_revenue_growth_rate.png"),
        Inches(6.2), Inches(1.3), Inches(7.0), Inches(5.2)
    )

    # Bottom callout bar
    bar = slide.shapes.add_shape(1, Inches(0.4), Inches(6.7),
                                 Inches(12.5), Inches(0.65))
    bar.fill.solid(); bar.fill.fore_color.rgb = BORDER
    bar.line.fill.background()
    add_text(slide,
             "Nike crossed below 0% growth in 2024 \u2014 the only brand in the room going backwards.",
             x=0.6, y=6.72, w=12.1, h=0.55,
             font="Calibri", size=12, color=BODY)


# ===========================================================================
# SLIDE 6 - CONSUMER VOICE
# ===========================================================================
def build_slide6(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "What Consumers Are Actually Saying",
              x=2.5, y=0.5, w=10.0, size=34)

    slide.shapes.add_picture(
        os.path.join(VIZ, "05_sentiment_scores.png"),
        Inches(0.4), Inches(1.3), Inches(7.5), Inches(5.0)
    )

    rx = 8.2

    add_text(slide, "KEY FINDING",
             x=rx, y=1.3, w=5.0, h=0.3,
             font="Calibri", size=11, color=MINT, bold=True)

    # Main finding box with left mint accent
    add_box(slide, x=rx, y=1.65, w=4.9, h=0.9)
    la = slide.shapes.add_shape(1, Inches(rx), Inches(1.65),
                                Inches(0.06), Inches(0.9))
    la.fill.solid(); la.fill.fore_color.rgb = MINT
    la.line.fill.background()
    add_text(slide,
             "Nike is the ONLY brand with negative consumer sentiment.",
             x=rx+0.15, y=1.7, w=4.6, h=0.8,
             font="Calibri", size=14, color=WHITE)

    # Score box - Nike
    add_box(slide, x=rx, y=2.7, w=4.9, h=0.85)
    add_text(slide, "-0.372",
             x=rx+0.15, y=2.72, w=2.2, h=0.55,
             font="Calibri", size=30, color=PURPLE, bold=True)
    add_text(slide, "Nike",
             x=rx+2.4, y=2.9, w=2.3, h=0.4,
             font="Calibri", size=11, color=MUTED)

    # Score box - New Balance
    add_box(slide, x=rx, y=3.65, w=4.9, h=0.85, border_color=MINT)
    add_text(slide, "+0.833",
             x=rx+0.15, y=3.67, w=2.2, h=0.55,
             font="Calibri", size=30, color=MINT, bold=True)
    add_text(slide, "New Balance",
             x=rx+2.4, y=3.85, w=2.3, h=0.4,
             font="Calibri", size=11, color=MUTED)

    add_text(slide,
             "Reddit, Amazon Reviews, Running Forums \u00b7 38 themes",
             x=rx, y=4.7, w=4.9, h=0.35,
             font="Calibri", size=10, color=MUTED)


# ===========================================================================
# SLIDE 7 - THE GAP
# ===========================================================================
def build_slide7(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "Category-by-Category: Where Nike Is Failing",
              x=2.5, y=0.4, w=10.5, size=34)

    slide.shapes.add_picture(
        os.path.join(VIZ, "06_sentiment_heatmap.png"),
        Inches(0.4), Inches(1.1), Inches(12.5), Inches(3.8)
    )

    rows = [
        (5.1,  "GenZ Appeal  -0.51",  "GenZ sees Nike as their parents\u2019 brand \u2014 #1 pain point by volume"),
        (5.75, "Availability  -1.00", "Bots and resellers destroyed the community drop culture"),
        (6.4,  "Pricing  -0.38",      "Too expensive for the quality consumers are getting"),
    ]
    for ry, label, desc in rows:
        add_box(slide, x=0.4, y=ry, w=12.5, h=0.55)
        # left purple accent
        la = slide.shapes.add_shape(1, Inches(0.4), Inches(ry),
                                    Inches(0.06), Inches(0.55))
        la.fill.solid(); la.fill.fore_color.rgb = PURPLE
        la.line.fill.background()
        add_text(slide, label,
                 x=0.6, y=ry+0.05, w=3.2, h=0.45,
                 font="Calibri", size=13, color=PURPLE, bold=True)
        add_text(slide, desc,
                 x=3.85, y=ry+0.05, w=9.0, h=0.45,
                 font="Calibri", size=13, color=BODY)


# ===========================================================================
# SLIDE 8 - THE WHITESPACE
# ===========================================================================
def build_slide8(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "The Opportunity: Nike Is in the Wrong Zone",
              x=2.5, y=0.4, w=10.5, size=34)

    add_text(slide,
             "Every competitor has moved to the Win Zone. Nike sits alone in the Danger Zone.",
             x=2.5, y=1.05, w=10.5, h=0.4,
             font="Calibri", size=14, color=BODY, italic=True)

    slide.shapes.add_picture(
        os.path.join(VIZ, "07_brand_positioning_map.png"),
        Inches(0.5), Inches(1.5), Inches(12.2), Inches(5.2)
    )

    bot = slide.shapes.add_shape(1, Inches(0.4), Inches(6.85),
                                 Inches(12.5), Inches(0.5))
    bot.fill.solid(); bot.fill.fore_color.rgb = BOX_BG
    bot.line.color.rgb = BORDER
    bot.line.width = Pt(1)
    add_text(slide,
             "Path forward: Earn back cultural authenticity \u2014 the one thing money alone cannot buy.",
             x=0.6, y=6.87, w=12.1, h=0.45,
             font="Calibri", size=12, color=MINT)


# ===========================================================================
# SLIDE 9 - THE STRATEGY
# ===========================================================================
def build_slide9(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "\u201cNike Reborn\u201d \u2014 A 3-Pillar GenZ Strategy",
              x=2.5, y=0.4, w=10.5, size=34)

    add_text(slide,
             "Data-Driven.  Culture-First.  Community-Led.",
             x=2.5, y=1.05, w=10.5, h=0.4,
             font="Calibri", size=14, color=MINT, bold=True)

    slide.shapes.add_picture(
        os.path.join(VIZ, "08_strategy_framework.png"),
        Inches(0.4), Inches(1.5), Inches(12.5), Inches(5.0)
    )

    # Footer purple boxes
    labels = ["Community-First Drops", "GenZ Co-Creation", "Cultural Partnerships"]
    xpos   = [0.35, 4.52, 8.68]
    for lbl, fx in zip(labels, xpos):
        fb = slide.shapes.add_shape(1, Inches(fx), Inches(6.75),
                                    Inches(4.0), Inches(0.55))
        fb.fill.solid(); fb.fill.fore_color.rgb = PURPLE
        fb.line.fill.background()
        add_text(slide, lbl, x=fx, y=6.77, w=4.0, h=0.5,
                 font="Calibri", size=12, color=WHITE,
                 align=PP_ALIGN.CENTER)


# ===========================================================================
# SLIDE 10 - CONCLUSION
# ===========================================================================
def build_slide10(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_corner_decoration(slide)

    add_title(slide, "If We Execute: A 3-Year Roadmap Back to Growth",
              x=2.5, y=0.4, w=10.5, size=34)

    slide.shapes.add_picture(
        os.path.join(VIZ, "09_projected_impact.png"),
        Inches(0.4), Inches(1.1), Inches(12.5), Inches(3.7)
    )

    results = [
        (0.35,  MINT,   "GenZ Search Index",   "30 \u2192 72  (+140%)", MINT),
        (4.52,  PURPLE, "Consumer Sentiment",  "-0.37 \u2192 +0.45",    PURPLE),
        (8.68,  MINT,   "Revenue Growth",      "-10% \u2192 +15%",      MINT),
    ]
    for rx, top_color, lbl, val, val_color in results:
        add_box(slide, x=rx, y=5.05, w=4.0, h=1.35,
                top_border_color=top_color, top_border_pt=3)
        add_text(slide, lbl,
                 x=rx+0.15, y=5.18, w=3.7, h=0.35,
                 font="Calibri", size=11, color=MUTED)
        add_text(slide, val,
                 x=rx+0.15, y=5.6, w=3.7, h=0.6,
                 font="Calibri", size=22, color=val_color, bold=True)

    add_text(slide,
             "\u201cNike doesn\u2019t need a new shoe. It needs a new relationship with the next generation.\u201d",
             x=0.4, y=6.55, w=12.5, h=0.65,
             font="Calibri", size=13, color=MUTED, italic=True)


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H

    print("Building slide 1 - Title ...")
    build_slide1(prs)
    print("Building slide 2 - The Shift ...")
    build_slide2(prs)
    print("Building slide 3 - Market Landscape ...")
    build_slide3(prs)
    print("Building slide 4 - The Challengers ...")
    build_slide4(prs)
    print("Building slide 5 - Nike By The Numbers ...")
    build_slide5(prs)
    print("Building slide 6 - Consumer Voice ...")
    build_slide6(prs)
    print("Building slide 7 - The Gap ...")
    build_slide7(prs)
    print("Building slide 8 - The Whitespace ...")
    build_slide8(prs)
    print("Building slide 9 - The Strategy ...")
    build_slide9(prs)
    print("Building slide 10 - Conclusion ...")
    build_slide10(prs)

    out = "/Users/vyankteshshimpi/Downloads/projects/Nike_Market_Analysis/Nike_Market_Analysis_Deck.pptx"
    prs.save(out)
    size_mb = os.path.getsize(out) / (1024 * 1024)
    print(f"\nSaved: {out}")
    print(f"File size: {size_mb:.2f} MB")


if __name__ == "__main__":
    main()
