import os
import sys
from academic_curriculum import ALL_TOPICS
from simulations import SIMULATIONS
from character_symbols import HERO_META
from marvel_missions import MISSIONS_DATA
from cursor_emblems import CURSOR_URLS, get_hero_cursor_url

output_dir = r"C:\Users\Babitha Ravindra\.gemini\antigravity\scratch\algo-vengers"

hero_png_map = {
    "ANT-MAN": "assets/antman.png",
    "DOCTOR STRANGE": "assets/doctorstrange.png",
    "VISION": "assets/vision.png",
    "CAPTAIN AMERICA": "assets/captainamerica.png",
    "HULK": "assets/hulk.png",
    "GROOT": "assets/groot.png",
    "IRON MAN": "assets/ironman.png",
    "SCARLET WITCH": "assets/scarletwitch.png",
    "HAWKEYE": "assets/hawkeye.png",
    "SPIDER-MAN": "assets/spiderman.png",
    "WAR MACHINE": "assets/warmachine.png",
    "QUICKSILVER": "assets/quicksilver.png",
    "BLACK PANTHER": "assets/blackpanther.png",
    "ROCKET RACCOON": "assets/rocket.png",
    "THOR": "assets/thor.png",
    "WOLVERINE": "assets/wolverine.png",
    "CAPTAIN MARVEL": "assets/captainmarvel.png",
    "LOKI": "assets/loki.png",
    "BLACK WIDOW": "assets/blackwidow.png"
}

def build_topic_page(t):
    hero_name = t["hero_name"]
    png_file = hero_png_map.get(hero_name, "assets/captainamerica.png")
    
    # Hero Character Meta
    meta = HERO_META.get(hero_name, {
        "symbol": "★",
        "symbol_name": "Hero Emblem",
        "hero_color": t["hero_color"],
        "badge_bg": t["badge_color"],
        "progress_gradient": "linear-gradient(90deg, #1d4ed8, #3b82f6, #60a5fa)",
        "cursor_badge": "★ HERO",
        "domain": "Algorithmic Tactics"
    })
    
    hero_symbol = meta["symbol"]
    hero_symbol_name = meta["symbol_name"]
    hero_color = meta["hero_color"]
    badge_bg = meta["badge_bg"]
    progress_gradient = meta["progress_gradient"]

    # Native CSS Circular Emblem Cursor for this Hero (Zero trailing lag, zero PNG cursors)
    hero_cursor_url = get_hero_cursor_url(hero_name)

    # Marvel Mission Narrative
    mission = MISSIONS_DATA.get(t["topic_id"], {
        "mission_code": f"OP-DAA-{t['topic_num']}",
        "mission_title": t["topic_title"].upper(),
        "story_intro": f"The Avengers defense network requires optimal deployment of {t['topic_title']}.",
        "problem_statement": f"Standard unoptimized algorithms fail under high-throughput battle conditions.",
        "why_algorithm": f"Optimizing this algorithm achieves provable asymptotic efficiency.",
        "objective": f"Master {t['topic_title']} and verify algorithmic invariants under pressure.",
        "success_state": "Mission complete! Optimal bounds secured!"
    })

    # Complexity Table rows
    table_rows = ""
    for row in t["complexity_table"]:
        col1 = row[0]
        col2 = row[1]
        col3 = row[2] if len(row) > 2 else ""
        col4 = row[3] if len(row) > 3 else ""
        table_rows += f"""
        <tr>
          <td style="font-weight: 600; color: #0f172a;">{col1}</td>
          <td><span class="complexity-badge">{col2}</span></td>
          <td style="font-family: var(--font-code); color: {hero_color}; font-weight: 600;">{col3}</td>
          <td style="color: #475569;">{col4}</td>
        </tr>"""

    # Speech Bubble 1: Tactical Intel
    spk1, quote1 = t["speech_bubbles"][0]
    speech_bubble_1 = f"""
    <div class="hero-speech-bubble" style="display: flex; align-items: flex-start; gap: 16px; background: #ffffff; border: 3px solid #0f172a; box-shadow: 0 4px 0 #0f172a; padding: 16px; margin: 24px 0;">
      <div style="width: 58px; height: 62px; background: {badge_bg}; border: 2px solid #0f172a; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        <img src="{png_file}" style="max-width: 50px; max-height: 54px; object-fit: contain; image-rendering: pixelated;" alt="{spk1}">
      </div>
      <div style="position: relative; flex: 1;">
        <div style="font-family: var(--font-pixel); font-size: 0.62rem; color: {hero_color}; margin-bottom: 4px;">
          [{hero_symbol}] COMM-LINK // {spk1}
        </div>
        <div style="font-size: 0.92rem; color: #1e293b; line-height: 1.6;">
          "{quote1}"
        </div>
      </div>
    </div>
    """

    # Speech Bubble 2: Algorithmic Invariant
    spk2, quote2 = t["speech_bubbles"][1]
    speech_bubble_2 = f"""
    <div class="hero-speech-bubble" style="display: flex; align-items: flex-start; gap: 16px; background: #ffffff; border: 3px solid #0f172a; box-shadow: 0 4px 0 #0f172a; padding: 16px; margin: 24px 0;">
      <div style="width: 58px; height: 62px; background: {badge_bg}; border: 2px solid #0f172a; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        <img src="{png_file}" style="max-width: 50px; max-height: 54px; object-fit: contain; image-rendering: pixelated;" alt="{spk2}">
      </div>
      <div style="position: relative; flex: 1;">
        <div style="font-family: var(--font-pixel); font-size: 0.62rem; color: {hero_color}; margin-bottom: 4px;">
          [{hero_symbol}] TACTICAL ADVICE // {spk2}
        </div>
        <div style="font-size: 0.92rem; color: #1e293b; line-height: 1.6;">
          "{quote2}"
        </div>
      </div>
    </div>
    """

    # Speech Bubble 3: Systems Takeaway
    speech_bubble_3 = f"""
    <div class="hero-speech-bubble" style="display: flex; align-items: flex-start; gap: 16px; background: #ffffff; border: 3px solid #0f172a; box-shadow: 0 4px 0 #0f172a; padding: 16px; margin: 24px 0;">
      <div style="width: 58px; height: 62px; background: {badge_bg}; border: 2px solid #0f172a; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        <img src="{png_file}" style="max-width: 50px; max-height: 54px; object-fit: contain; image-rendering: pixelated;" alt="{hero_name}">
      </div>
      <div style="position: relative; flex: 1;">
        <div style="font-family: var(--font-pixel); font-size: 0.62rem; color: {hero_color}; margin-bottom: 4px;">
          [{hero_symbol}] S.H.I.E.L.D. FIELD DIRECTIVE // {hero_name}
        </div>
        <div style="font-size: 0.92rem; color: #1e293b; line-height: 1.6;">
          "{t['hero_quote']}" Remember: asymptotic guarantees hold when n grows large, but cache coherence, memory layout, and branch prediction dominate for small inputs in production hardware.
        </div>
      </div>
    </div>
    """

    # Simulation engine
    sim = SIMULATIONS.get(t["viz_type"])
    if sim:
        viz_html = sim["html"]
        viz_script = sim["script"]
    else:
        viz_html = "<div style='padding:20px; text-align:center;'>Simulation engine loading...</div>"
        viz_script = "// No sim script"

    # Quiz HTML builder
    quiz_html = ""
    quiz_data_js = []
    for q_idx, q in enumerate(t["quiz"]):
        opt_html = ""
        for o_idx, opt in enumerate(q["options"]):
            opt_html += f"""
            <button class="quiz-opt-btn" data-qid="{q_idx}" data-oid="{o_idx}" style="text-align: left; padding: 10px 14px; background: #f8fafc; border: 2px solid #0f172a; font-size: 0.88rem; font-family: var(--font-body); font-weight: 600; color: #0f172a; transition: all 0.15s ease; box-shadow: 0 2px 0 #0f172a;">
              <span style="font-family: var(--font-pixel); font-size: 0.62rem; margin-right: 8px; color: {hero_color};">[{chr(65+o_idx)}]</span> {opt}
            </button>
            """
        quiz_html += f"""
        <div class="quiz-card" id="quiz-card-{q_idx}" style="background: #ffffff; border: 2px solid #0f172a; padding: 18px; margin-bottom: 16px; box-shadow: 0 4px 0 #0f172a;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-family: var(--font-pixel); font-size: 0.68rem; color: {hero_color};">QUESTION {q_idx+1} OF {len(t["quiz"])}</span>
            <span class="quiz-status-tag" id="quiz-status-{q_idx}" style="font-family: var(--font-pixel); font-size: 0.58rem; background: #e2e8f0; color: #475569; padding: 4px 8px;">UNANSWERED</span>
          </div>
          <div style="font-size: 0.95rem; font-weight: 600; color: #0f172a; margin-bottom: 14px; line-height: 1.5;">
            {q["q"]}
          </div>
          <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-bottom: 12px;">
            {opt_html}
          </div>
          <div class="quiz-feedback-box" id="quiz-feedback-{q_idx}" style="display: none; padding: 12px 14px; border: 2px solid #0f172a; font-size: 0.85rem; line-height: 1.6; margin-top: 10px;">
          </div>
        </div>
        """
        quiz_data_js.append({
            "answer": q["answer"],
            "explanation": q["explanation"]
        })

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t["topic_title"]} // [{hero_symbol}] {hero_name} — ALGO-VENGERS</title>
  
  <meta name="description" content="Design & Analysis of Algorithms: {t["topic_title"]}. Mission {t["mission_num"]}: {t["mission_title"]}.">
  <meta name="theme-color" content="#f8fafc">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Press+Start+2P&family=Silkscreen:wght@400;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

  <!-- KaTeX for beautiful math formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <style>
    :root {{
      --bg-main: #f8fafc;
      --border-dark: #0f172a;
      --text-main: #0f172a;
      --text-muted: #475569;
      --color-gold: #d97706;
      --color-cyan: #0284c7;
      --hero-accent: {hero_color};
      --badge-bg: {badge_bg};

      --font-pixel: 'Press Start 2P', monospace;
      --font-pixel-sub: 'Silkscreen', monospace;
      --font-body: 'Plus Jakarta Sans', system-ui, sans-serif;
      --font-code: 'JetBrains Mono', monospace;
      --top-bar-height: 32px;
      --nav-height: 72px;
      --container-max: 1100px;
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    /* Pixelated retro mouse pointer */
    html, body {{
      scroll-behavior: smooth;
      font-size: 16px;
      background-color: var(--bg-main);
      color: var(--text-main);
      font-family: var(--font-body);
      cursor: {CURSOR_URLS['arrow']} !important;
    }}
    
    body {{
      overflow-x: hidden;
      min-height: 100vh;
      line-height: 1.6;
      display: flex;
      flex-direction: column;
      background-color: var(--bg-main);
    }}

    /* Native CSS Circular Hero Emblem Cursor on all interactive elements (ZERO TRAILING) */
    a, button, .pixel-btn, .topic-card, .mission-card, input, select, label, .top-progress-track-wrapper, .hero-speech-bubble, [role="button"], [data-hero-cursor], .quiz-opt-btn {{
      cursor: {hero_cursor_url} !important;
    }}

    .cyber-grid-bg {{
      position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background-image: linear-gradient(to right, rgba(15, 23, 42, 0.05) 1px, transparent 1px), linear-gradient(to bottom, rgba(15, 23, 42, 0.05) 1px, transparent 1px);
      background-size: 32px 32px; pointer-events: none; z-index: 0;
    }}
    .container {{ max-width: var(--container-max); margin: 0 auto; padding: 0 24px; position: relative; z-index: 2; }}
    .pixel-heading {{ font-family: var(--font-pixel); letter-spacing: 1px; text-transform: uppercase; }}

    /* Pixel Buttons */
    .pixel-btn {{
      display: inline-flex; align-items: center; justify-content: center; gap: 8px;
      padding: 10px 18px; font-family: var(--font-pixel); font-size: 0.65rem;
      text-decoration: none; text-transform: uppercase; border: 3px solid var(--border-dark);
      position: relative; user-select: none;
      transition: transform 0.1s ease, box-shadow 0.1s ease;
      box-shadow: -3px 0 0 0 var(--border-dark), 3px 0 0 0 var(--border-dark), 0 -3px 0 0 var(--border-dark), 0 3px 0 0 var(--border-dark), 0 4px 0 0 var(--border-dark);
    }}
    .pixel-btn:hover {{ transform: translateY(-2px); box-shadow: -3px 0 0 0 var(--border-dark), 3px 0 0 0 var(--border-dark), 0 -3px 0 0 var(--border-dark), 0 3px 0 0 var(--border-dark), 0 6px 0 0 var(--border-dark); }}
    .pixel-btn:active {{ transform: translateY(2px); box-shadow: -3px 0 0 0 var(--border-dark), 3px 0 0 0 var(--border-dark), 0 -3px 0 0 var(--border-dark), 0 3px 0 0 var(--border-dark), 0 2px 0 0 var(--border-dark); }}
    .pixel-btn-primary {{ background: #facc15; color: #0f172a; font-weight: bold; }}
    .pixel-btn-secondary {{ background: #ffffff; color: var(--color-cyan); }}
    .pixel-btn-accent {{ background: var(--hero-accent); color: #ffffff; }}

    /* Sticky Navbar */
    .pixel-navbar {{
      position: fixed; top: var(--top-bar-height); left: 0; width: 100%; height: var(--nav-height);
      background: rgba(255, 255, 255, 0.96); backdrop-filter: blur(10px);
      border-bottom: 3px solid var(--border-dark); z-index: 1000; display: flex; align-items: center;
    }}
    .nav-container {{ display: flex; align-items: center; justify-content: space-between; width: 100%; max-width: var(--container-max); margin: 0 auto; padding: 0 24px; }}
    .nav-brand {{ display: flex; align-items: center; gap: 12px; text-decoration: none; }}
    .brand-icon {{ width: 36px; height: 36px; background: #facc15; border: 2px solid var(--border-dark); display: flex; align-items: center; justify-content: center; }}
    .brand-icon svg {{ width: 22px; height: 22px; fill: var(--border-dark); }}
    .brand-text {{ font-family: var(--font-pixel); font-size: 1.05rem; color: var(--border-dark); }}
    .brand-text span {{ color: #dc2626; }}
    .breadcrumbs {{ font-family: var(--font-pixel); font-size: 0.6rem; color: var(--text-muted); display: flex; align-items: center; gap: 6px; }}
    .breadcrumbs a {{ color: var(--color-cyan); text-decoration: none; }}

    /* Persistent Top Reading Progress Bar */
    #global-top-progress {{
      position: fixed; top: 0; left: 0; width: 100%; height: var(--top-bar-height);
      background: #0f172a; border-bottom: 2px solid #000; z-index: 10002;
      display: flex; align-items: center; justify-content: space-between; padding: 0 16px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    }}
    .top-progress-hero-badge {{
      display: flex; align-items: center; gap: 8px; flex-shrink: 0;
    }}
    .top-hero-symbol-box {{
      width: 22px; height: 22px; background: {badge_bg}; color: {hero_color};
      border: 1.5px solid {hero_color}; font-family: var(--font-pixel); font-size: 0.75rem;
      display: flex; align-items: center; justify-content: center; border-radius: 2px;
    }}
    .top-hero-title {{
      font-family: var(--font-pixel); font-size: 0.58rem; color: #f8fafc; letter-spacing: 0.5px;
    }}
    .top-progress-track-wrapper {{
      flex: 1; max-width: 650px; margin: 0 20px; height: 10px; background: #1e293b;
      border: 1.5px solid #475569; border-radius: 999px; position: relative; cursor: pointer;
    }}
    .top-progress-fill-bar {{
      height: 100%; width: 0%; background: {progress_gradient}; border-radius: 999px;
      transition: width 0.08s ease-out;
    }}
    .top-progress-slider-marker {{
      position: absolute; top: 50%; left: 0%; transform: translate(-50%, -50%);
      width: 22px; height: 22px; background: #0f172a; border: 2px solid {hero_color};
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
      font-family: var(--font-pixel); font-size: 0.65rem; color: {hero_color};
      box-shadow: 0 0 10px {hero_color}; pointer-events: none; transition: left 0.08s ease-out;
    }}
    .top-progress-percent-readout {{
      font-family: var(--font-pixel); font-size: 0.65rem; color: #facc15; min-width: 50px; text-align: right; flex-shrink: 0;
    }}

    /* Main Container */
    main {{ flex: 1; padding-top: calc(var(--nav-height) + var(--top-bar-height) + 24px); padding-bottom: 60px; }}

    /* Topic Hero Section */
    .topic-hero {{
      background: #ffffff; border: 3px solid var(--border-dark);
      box-shadow: 0 6px 0 var(--border-dark); padding: 32px;
      margin-bottom: 32px; display: grid; grid-template-columns: auto 1fr; gap: 28px; align-items: center;
    }}
    .hero-sprite-frame {{
      width: 120px; height: 130px; background: var(--badge-bg);
      border: 3px solid var(--border-dark); display: flex; align-items: center; justify-content: center;
      position: relative; box-shadow: 0 4px 0 var(--border-dark); overflow: hidden;
    }}
    .hero-avatar-img {{
      max-width: 100px; max-height: 112px; width: auto; height: auto;
      object-fit: contain; image-rendering: pixelated;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.25)); transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .topic-hero:hover .hero-avatar-img {{ transform: scale(1.1) translateY(-3px); }}

    .hero-meta-tag {{
      display: inline-block; font-family: var(--font-pixel); font-size: 0.6rem;
      background: #ffffff; border: 2px solid var(--border-dark); padding: 3px 10px;
      margin-bottom: 10px; font-weight: bold; color: var(--hero-accent); box-shadow: 0 2px 0 var(--border-dark);
    }}
    .hero-title {{ font-size: 1.6rem; margin-bottom: 12px; line-height: 1.3; color: var(--border-dark); }}
    .hero-tagline {{ font-family: var(--font-code); font-size: 0.95rem; color: var(--text-muted); margin-bottom: 14px; font-weight: 600; }}
    .hero-quote-box {{
      background: #f1f5f9; border-left: 4px solid var(--hero-accent);
      padding: 10px 14px; font-style: italic; color: #1e293b; font-size: 0.88rem;
    }}

    /* Content Cards */
    .content-card {{
      background: #ffffff; border: 3px solid var(--border-dark);
      box-shadow: 0 5px 0 var(--border-dark); padding: 28px; margin-bottom: 28px;
    }}
    .card-heading {{
      display: flex; justify-content: space-between; align-items: center;
      font-family: var(--font-pixel); font-size: 0.85rem; color: var(--border-dark);
      margin-bottom: 18px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;
    }}
    .card-desc-text {{ font-size: 0.95rem; color: #1e293b; line-height: 1.7; margin-bottom: 16px; }}
    
    .math-callout {{
      background: #f1f5f9; border: 2px solid var(--border-dark); padding: 16px 20px;
      font-size: 0.95rem; margin-bottom: 16px; color: #0f172a;
      box-shadow: 0 3px 0 var(--border-dark); overflow-x: auto;
    }}

    /* Table */
    .algo-table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; }}
    .algo-table th, .algo-table td {{ border: 2px solid var(--border-dark); padding: 12px 14px; text-align: left; }}
    .algo-table th {{ background: #f8fafc; font-family: var(--font-pixel); font-size: 0.65rem; color: var(--border-dark); }}
    .complexity-badge {{
      display: inline-block; font-family: var(--font-code); font-weight: bold;
      background: var(--badge-bg); color: var(--hero-accent); border: 1px solid var(--hero-accent);
      padding: 3px 8px; border-radius: 4px; font-size: 0.85rem;
    }}

    /* Code Block */
    .code-box {{
      background: #0f172a; color: #f8fafc; border: 3px solid var(--border-dark);
      padding: 20px; font-family: var(--font-code); font-size: 0.85rem; line-height: 1.6;
      overflow-x: auto; position: relative; box-shadow: 0 5px 0 var(--border-dark);
    }}
    .code-header {{
      display: flex; justify-content: space-between; align-items: center;
      margin-bottom: 10px; font-family: var(--font-pixel); font-size: 0.65rem; color: #94a3b8;
    }}

    /* Interactive Visualizer Canvas */
    .viz-container {{
      background: #f8fafc; border: 2px dashed var(--border-dark); padding: 20px;
      border-radius: 4px; display: flex; flex-direction: column; align-items: center; gap: 16px;
    }}

    /* Speech Bubble */
    .hero-speech-bubble {{ transition: transform 0.15s ease; }}
    .hero-speech-bubble:hover {{ transform: translateY(-2px); }}

    /* Bottom Actions */
    .bottom-section {{
      text-align: center; margin-top: 30px; display: flex; flex-direction: column;
      align-items: center; gap: 16px;
    }}
    .pixel-divider {{ width: 180px; height: 4px; background: repeating-linear-gradient(to right, var(--border-dark) 0px, var(--border-dark) 8px, transparent 8px, transparent 16px); }}
  </style>
</head>
<body>

  <div class="cyber-grid-bg"></div>

  <!-- Persistent Top Reading Progress Bar -->
  <div id="global-top-progress">
    <div class="top-progress-hero-badge">
      <div class="top-hero-symbol-box">[{hero_symbol}]</div>
      <div class="top-hero-title">{hero_name} // {hero_symbol_name}</div>
    </div>
    <div class="top-progress-track-wrapper" id="global-progress-track" title="Click anywhere along the bar to jump in the dossier">
      <div class="top-progress-fill-bar" id="global-progress-fill"></div>
      <div class="top-progress-slider-marker" id="global-progress-marker">{hero_symbol}</div>
    </div>
    <div class="top-progress-percent-readout" id="global-progress-pct">0%</div>
  </div>

  <!-- Sticky Navbar -->
  <header class="pixel-navbar">
    <div class="nav-container">
      <a href="index.html" class="nav-brand">
        <div class="brand-icon"><svg viewBox="0 0 24 24"><polygon points="12,2 8,20 11,20 12,14 16,14 17,20 20,20 15,2"/><polygon points="12,6 10,12 14,12" fill="#facc15"/></svg></div>
        <div class="brand-text">ALGO-<span>VENGERS</span></div>
      </a>

      <div class="breadcrumbs">
        <a href="index.html">HQ</a> <span>▶</span>
        <a href="missions.html">MISSIONS</a> <span>▶</span>
        <a href="{t["mission_url"]}">MISSION {t["mission_num"]}</a> <span>▶</span>
        <span style="color: var(--border-dark); font-weight: bold;">{t["topic_num"]}</span>
      </div>

      <div>
        <a href="{t["mission_url"]}" class="pixel-btn pixel-btn-secondary" style="padding: 6px 12px; font-size: 0.6rem;">← MISSION HUB</a>
      </div>
    </div>
  </header>

  <main>
    <div class="container">

      <!-- Topic Hero Section -->
      <section class="topic-hero">
        <div class="hero-sprite-frame">
          <img src="{png_file}" alt="{hero_name}" class="hero-avatar-img">
        </div>
        <div>
          <span class="hero-meta-tag">MISSION {t["mission_num"]} // [{hero_symbol}] {hero_name}</span>
          <h1 class="hero-title pixel-heading">{t["topic_title"]}</h1>
          <div class="hero-tagline">{t["hero_tag"]} // {meta.get("domain", "Algorithmic Tactics")}</div>
          <div class="hero-quote-box">"{t["hero_quote"]}"</div>
        </div>
      </section>

      <!-- 01. S.H.I.E.L.D. Mission Briefing & Marvel Story -->
      <section class="content-card" style="border-left: 6px solid {hero_color};">
        <h2 class="card-heading">
          <span>01. S.H.I.E.L.D. MISSION BRIEFING // {mission["mission_code"]}</span>
          <span style="font-size: 0.6rem; color: var(--hero-accent);">{mission["mission_title"]}</span>
        </h2>
        <div class="card-desc-text" style="font-size: 1.02rem; font-weight: 500; color: #0f172a; margin-bottom: 12px;">
          {mission["story_intro"]}
        </div>
        <div style="background: #f1f5f9; border: 2px dashed #475569; padding: 12px 16px; margin-bottom: 10px;">
          <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #dc2626; margin-bottom: 4px;">CRITICAL CRISIS:</div>
          <div style="font-size: 0.9rem; color: #334155;">{mission["problem_statement"]}</div>
        </div>
        <div style="background: #ecfdf5; border: 2px solid #10b981; padding: 12px 16px;">
          <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #059669; margin-bottom: 4px;">TACTICAL OBJECTIVE:</div>
          <div style="font-size: 0.9rem; color: #065f46;">{mission["objective"]}</div>
        </div>
      </section>

      <!-- 02. Formal Specification & Problem Invariants -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>02. FORMAL PROBLEM SPECIFICATION & INVARIANTS</span>
          <span style="font-size: 0.6rem; color: var(--hero-accent);">ACADEMIC CURRICULUM</span>
        </h2>
        <div class="card-desc-text">{t["problem_invariants"]}</div>
      </section>

      <!-- Speech Bubble Callout 1 -->
      {speech_bubble_1}

      <!-- 03. Naive Approach vs Optimal Formulation -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>03. BRUTE FORCE VS ALGORITHMIC OPTIMALITY</span>
          <span style="font-size: 0.6rem; color: var(--color-gold);">STRATEGIC COMPARISON</span>
        </h2>
        <div class="card-desc-text">{t["naive_vs_optimal"]}</div>
        <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 12px 16px; margin-top: 12px;">
          <div style="font-family: var(--font-pixel); font-size: 0.6rem; color: #1d4ed8; margin-bottom: 4px;">WHY THIS ALGORITHM WINS:</div>
          <div style="font-size: 0.9rem; color: #1e3a8a;">{mission["why_algorithm"]}</div>
        </div>
      </section>

      <!-- 04. Mathematical Formulation & Recurrence Derivation -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>04. MATHEMATICAL PROOFS & RECURRENCES</span>
          <span style="font-size: 0.6rem; color: #2563eb;">KATEX FORMULATION</span>
        </h2>
        <div class="math-callout">{t["math_formulation"]}</div>
      </section>

      <!-- Speech Bubble Callout 2 -->
      {speech_bubble_2}

      <!-- 05. Concrete Worked Numerical Example -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>05. STEP-BY-STEP WORKED CALCULATION EXAMPLE</span>
          <span style="font-size: 0.6rem; color: #16a34a;">NUMERICAL TRACE</span>
        </h2>
        <div class="card-desc-text">{t["worked_example"]}</div>
      </section>

      <!-- 06. Interactive Physical Tactical Simulation Arena -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>06. RETRO PHYSICAL GAME SIMULATION & YOUR CUSTOM INPUTS</span>
          <span style="font-size: 0.6rem; color: var(--color-cyan);">LIVE SIMULATION CONSOLE</span>
        </h2>
        <div class="viz-container">
          <div class="sim-tactical-header" style="display: flex; align-items: center; justify-content: space-between; width: 100%; margin-bottom: 16px; padding: 12px 18px; background: #0f172a; border: 3px solid var(--border-dark); color: #f8fafc; box-shadow: 0 4px 0 var(--border-dark);">
            <div style="display: flex; align-items: center; gap: 14px;">
              <div style="width: 52px; height: 56px; background: {badge_bg}; border: 2px solid #ffffff; display: flex; align-items: center; justify-content: center; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.4);">
                <img src="{png_file}" style="max-width: 46px; max-height: 50px; width: auto; height: auto; object-fit: contain; image-rendering: pixelated;" alt="{hero_name}">
              </div>
              <div>
                <div style="font-family: var(--font-pixel); font-size: 0.7rem; color: #facc15;">OPERATOR: [{hero_symbol}] {hero_name}</div>
                <div style="font-family: var(--font-pixel-sub); font-size: 0.8rem; color: #94a3b8;">TACTICAL DAA PHYSICAL SIMULATION ENGINE</div>
              </div>
            </div>
            <div style="font-family: var(--font-pixel); font-size: 0.6rem; background: #1e293b; color: #22c55e; padding: 6px 12px; border: 1px solid #475569;">
              STATUS: READY
            </div>
          </div>
          {viz_html}
        </div>
      </section>

      <!-- 07. Asymptotic Derivation & Complexity Matrix -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>07. ASYMPTOTIC COMPLEXITY DERIVATION MATRIX</span>
          <span style="font-size: 0.6rem; color: var(--hero-accent);">DAA BIG-O BOUNDS</span>
        </h2>
        <table class="algo-table">
          <thead>
            <tr>
              <th>OPERATION / CASE</th>
              <th>ASYMPTOTIC BOUND</th>
              <th>SPACE / FOOTPRINT</th>
              <th>MATHEMATICAL INVARIANT</th>
            </tr>
          </thead>
          <tbody>
            {table_rows}
          </tbody>
        </table>
      </section>

      <!-- 08. Interactive Asymptotic Growth Comparison Slider -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>08. ASYMPTOTIC GROWTH COMPARISON</span>
          <span style="font-size: 0.6rem; color: var(--color-gold);">LIVE CALCULATOR</span>
        </h2>
        <div style="margin-bottom: 16px;">
          <p class="card-desc-text">Drag the input size slider \(n\) to observe step counts diverge across complexity classes in real-time:</p>
          <div style="background: #f1f5f9; border: 2px solid #0f172a; padding: 14px; margin-bottom: 14px; display: flex; align-items: center; justify-content: space-between; gap: 14px; flex-wrap: wrap;">
            <div style="display: flex; align-items: center; gap: 12px;">
              <label style="font-family: var(--font-pixel); font-size: 0.68rem; color: #0f172a;">INPUT SIZE (N):</label>
              <input type="range" id="growth-slider" min="1" max="10" value="4" style="width: 160px; accent-color: {hero_color};">
              <span id="growth-n-val" style="font-family: var(--font-code); font-weight: bold; background: #0f172a; color: #facc15; padding: 4px 10px; border-radius: 4px;">n = 16</span>
            </div>
            <div style="font-size: 0.8rem; color: #475569;">
              Compare: \(O(1), O(\log n), O(n), O(n \log n), O(n^2), O(2^n)\)
            </div>
          </div>
          
          <div id="growth-bars-container" style="display: flex; flex-direction: column; gap: 10px; background: #ffffff; border: 2px solid #0f172a; padding: 16px;">
            <!-- Dynamically populated via JS -->
          </div>
        </div>
      </section>

      <!-- 09. Practical Systems Design & Code Implementation -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>09. PRACTICAL SYSTEMS DESIGN & REFERENCE IMPLEMENTATION</span>
          <span style="font-size: 0.6rem; color: #8b5cf6;">PRODUCTION ARCHITECTURE</span>
        </h2>
        <div class="card-desc-text">{t["practical_considerations"]}</div>
        
        <div class="code-box" style="margin-top: 18px;">
          <div class="code-header">
            <span>ALGORITHM SPECIFICATION // PYTHON 3</span>
            <span>UTF-8 // VERIFIED OPTIMAL</span>
          </div>
          <pre><code>{t["code"]}</code></pre>
        </div>
      </section>

      <!-- Speech Bubble Callout 3 -->
      {speech_bubble_3}

      <!-- 10. Interactive Mini Quiz (4 Questions) -->
      <section class="content-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; border-bottom: 2px solid #e2e8f0; padding-bottom: 12px; flex-wrap: wrap; gap: 8px;">
          <h2 class="card-heading" style="margin-bottom: 0; border-bottom: none; padding-bottom: 0;">
            <span>10. MISSION ASSESSMENT // TEST YOUR MASTERY</span>
          </h2>
          <div style="font-family: var(--font-pixel); font-size: 0.68rem; background: #0f172a; color: #22c55e; padding: 6px 12px; border: 2px solid var(--border-dark);" id="quiz-score-badge">
            SCORE: 0 / {len(t["quiz"])} (0%)
          </div>
        </div>
        <p class="card-desc-text">Test your mastery of {t["topic_title"]} with these university exam questions:</p>
        <div>
          {quiz_html}
        </div>
      </section>

      <!-- 11. Key Exam Takeaways -->
      <section class="content-card">
        <h2 class="card-heading">
          <span>11. S.H.I.E.L.D. DEBRIEF & KEY EXAM TAKEAWAYS</span>
          <span style="font-size: 0.6rem; color: var(--border-dark);">REVISION CHECKLIST</span>
        </h2>
        <p class="card-desc-text">{t["summary"]}</p>
      </section>

      <!-- Navigation & Return -->
      <section class="bottom-section">
        <div class="pixel-divider"></div>
        <div style="display: flex; gap: 14px; margin-top: 8px; flex-wrap: wrap; justify-content: center;">
          <a href="{t["mission_url"]}" class="pixel-btn pixel-btn-primary">← BACK TO MISSION {t["mission_num"]}</a>
          <a href="missions.html" class="pixel-btn pixel-btn-secondary">ALL MISSIONS</a>
          <a href="index.html" class="pixel-btn pixel-btn-accent">RETURN TO HQ</a>
        </div>
      </section>

    </div>
  </main>

  <footer style="background: #0f172a; color: #f8fafc; border-top: 3px solid #000; padding: 24px 0; text-align: center; font-family: var(--font-pixel); font-size: 0.62rem; margin-top: 40px;">
    <div class="container">
      ALGO-VENGERS // DESIGN & ANALYSIS OF ALGORITHMS // S.H.I.E.L.D. DATABASE
    </div>
  </footer>

  <script>
    /* Retro Web Audio Engine */
    class RetroAudioEngine {{
      constructor() {{
        this.ctx = null;
        this.init();
      }}
      init() {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) this.ctx = new AudioContext();
      }}
      ensure() {{
        if (this.ctx && this.ctx.state === 'suspended') this.ctx.resume();
      }}
      playTone(freq, type, duration, vol=0.1) {{
        try {{
          this.ensure();
          if (!this.ctx) return;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          gain.gain.setValueAtTime(vol, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        }} catch(e) {{}}
      }}
      playClick() {{ this.playTone(600, 'square', 0.05, 0.08); }}
      playHover() {{ this.playTone(400, 'sine', 0.03, 0.04); }}
      playSuccess() {{
        try {{
          this.ensure();
          if (!this.ctx) return;
          const now = this.ctx.currentTime;
          [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {{
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, now + idx * 0.08);
            gain.gain.setValueAtTime(0.08, now + idx * 0.08);
            gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.15);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + idx * 0.08);
            osc.stop(now + idx * 0.08 + 0.15);
          }});
        }} catch(e) {{}}
      }}
      playError() {{
        try {{
          this.ensure();
          if (!this.ctx) return;
          const now = this.ctx.currentTime;
          [220, 164.81].forEach((freq, idx) => {{
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(freq, now + idx * 0.1);
            gain.gain.setValueAtTime(0.08, now + idx * 0.1);
            gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.1 + 0.15);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + idx * 0.1);
            osc.stop(now + idx * 0.1 + 0.15);
          }});
        }} catch(e) {{}}
      }}
    }}
    const retroAudio = new RetroAudioEngine();

    const interactiveQuery = 'a, button, .pixel-btn, .topic-card, .mission-card, input, select, label, .top-progress-track-wrapper, .hero-speech-bubble, [role="button"], [data-hero-cursor], .quiz-opt-btn';

    document.addEventListener('mouseover', (e) => {{
      if (e.target.closest(interactiveQuery)) {{
        retroAudio.playHover();
      }}
    }});

    /* Persistent Top Reading Progress Bar */
    const topFillBar = document.getElementById('global-progress-fill');
    const topMarker = document.getElementById('global-progress-marker');
    const topPct = document.getElementById('global-progress-pct');
    const topTrack = document.getElementById('global-progress-track');

    function updateTopReadingProgress() {{
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? Math.min(100, Math.max(0, Math.round((scrollTop / docHeight) * 100))) : 0;
      
      if (topFillBar) topFillBar.style.width = pct + '%';
      if (topPct) topPct.textContent = pct + '%';
      if (topMarker) {{
        topMarker.style.left = pct + '%';
      }}
    }}

    window.addEventListener('scroll', updateTopReadingProgress, {{ passive: true }});
    updateTopReadingProgress();

    topTrack?.addEventListener('click', (e) => {{
      const rect = topTrack.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = Math.max(0, Math.min(1, clickX / rect.width));
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      window.scrollTo({{ top: ratio * docHeight, behavior: 'smooth' }});
      retroAudio.playClick();
    }});

    /* Asymptotic Growth Comparison Slider */
    const growthSlider = document.getElementById('growth-slider');
    const growthNVal = document.getElementById('growth-n-val');
    const growthBarsContainer = document.getElementById('growth-bars-container');
    const nPowers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024];

    function renderGrowthBars() {{
      const idx = parseInt(growthSlider.value) - 1;
      const n = nPowers[idx];
      growthNVal.textContent = `n = ${{n}}`;
      
      const c_const = 1;
      const c_log = Math.round(Math.log2(n) * 10) / 10;
      const c_lin = n;
      const c_nlogn = Math.round(n * Math.log2(n));
      const c_quad = n * n;
      const c_exp = n <= 32 ? Math.pow(2, n) : '1.79e+308+';

      const classes = [
        {{ name: 'O(1) Constant', ops: c_const, color: '#22c55e', pct: 2 }},
        {{ name: 'O(log n) Logarithmic', ops: c_log, color: '#38bdf8', pct: Math.min(100, (c_log / 10) * 12) }},
        {{ name: 'O(n) Linear', ops: c_lin, color: '#facc15', pct: Math.min(100, (c_lin / 1024) * 45) }},
        {{ name: 'O(n log n) Linearithmic', ops: c_nlogn, color: '#f97316', pct: Math.min(100, (c_nlogn / 10240) * 70) }},
        {{ name: 'O(n^2) Quadratic', ops: c_quad, color: '#ef4444', pct: Math.min(100, Math.max(10, (c_quad / 1000000) * 100)) }},
        {{ name: 'O(2^n) Exponential', ops: c_exp, color: '#881337', pct: 100 }}
      ];

      growthBarsContainer.innerHTML = classes.map(c => `
        <div>
          <div style="display: flex; justify-content: space-between; font-family: var(--font-pixel); font-size: 0.62rem; margin-bottom: 4px;">
            <span style="color: ${{c.color}};">${{c.name}}</span>
            <span style="font-family: var(--font-code); font-weight: bold; color: #0f172a;">${{typeof c.ops === 'number' ? c.ops.toLocaleString() : c.ops}} operations</span>
          </div>
          <div style="width: 100%; height: 14px; background: #f1f5f9; border: 1.5px solid #0f172a; border-radius: 2px; overflow: hidden;">
            <div style="width: ${{c.pct}}%; height: 100%; background: ${{c.color}}; transition: width 0.3s ease;"></div>
          </div>
        </div>
      `).join('');
    }}

    growthSlider?.addEventListener('input', () => {{
      renderGrowthBars();
      retroAudio.playHover();
    }});
    renderGrowthBars();

    /* Interactive Mini-Quiz Logic */
    const quizData = {quiz_data_js};
    let quizScore = 0;
    const answeredQuestions = new Set();

    document.querySelectorAll('.quiz-opt-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const qid = parseInt(btn.dataset.qid);
        const oid = parseInt(btn.dataset.oid);
        if (answeredQuestions.has(qid)) return;
        answeredQuestions.add(qid);

        const q = quizData[qid];
        const card = document.getElementById(`quiz-card-${{qid}}`);
        const statusTag = document.getElementById(`quiz-status-${{qid}}`);
        const feedbackBox = document.getElementById(`quiz-feedback-${{qid}}`);
        const allOpts = card.querySelectorAll('.quiz-opt-btn');

        allOpts.forEach((b, idx) => {{
          if (idx === q.answer) {{
            b.style.background = '#dcfce7';
            b.style.borderColor = '#16a34a';
            b.style.color = '#15803d';
          }} else if (idx === oid && oid !== q.answer) {{
            b.style.background = '#fee2e2';
            b.style.borderColor = '#ef4444';
            b.style.color = '#b91c1c';
          }}
          b.disabled = true;
        }});

        feedbackBox.style.display = 'block';
        if (oid === q.answer) {{
          quizScore++;
          retroAudio.playSuccess();
          statusTag.textContent = 'CORRECT';
          statusTag.style.background = '#dcfce7';
          statusTag.style.color = '#16a34a';
          feedbackBox.style.background = '#f0fdf4';
          feedbackBox.style.borderColor = '#16a34a';
          feedbackBox.innerHTML = `<strong>✨ EXCELLENT WORK!</strong><br>${{q.explanation}}`;
        }} else {{
          retroAudio.playError();
          statusTag.textContent = 'INCORRECT';
          statusTag.style.background = '#fee2e2';
          statusTag.style.color = '#ef4444';
          feedbackBox.style.background = '#fef2f2';
          feedbackBox.style.borderColor = '#ef4444';
          feedbackBox.innerHTML = `<strong>⚠️ TACTICAL REVIEW:</strong><br>${{q.explanation}}`;
        }}

        const pct = Math.round((quizScore / quizData.length) * 100);
        const scoreBadge = document.getElementById('quiz-score-badge');
        if (scoreBadge) scoreBadge.textContent = `SCORE: ${{quizScore}} / ${{quizData.length}} (${{pct}}%)`;
      }});
    }});

    // KaTeX Auto-Render Math
    document.addEventListener("DOMContentLoaded", function() {{
      if (typeof renderMathInElement !== 'undefined') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: "$$", right: "$$", display: true}},
            {{left: "\\\[", right: "\\\]", display: true}},
            {{left: "$", right: "$", display: false}},
            {{left: "\\\(", right: "\\\)", display: false}}
          ],
          throwOnError: false
        }});
      }}
    }});

    // Visualizer Specific Game Loop Logic
    {viz_script}
  </script>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    # Generate all 19 topics
    print(f"Beginning generation of {len(ALL_TOPICS)} comprehensive academic topic pages...")
    for t in ALL_TOPICS:
        filepath = os.path.join(output_dir, t["filename"])
        content = build_topic_page(t)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {t['filename']}")

    print("All 19 academic topic pages successfully generated with native circular emblem cursors and persistent top reading progress bar!")
