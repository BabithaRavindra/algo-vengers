# update_all_hub_pages.py - Updates all 7 Hub Pages with:
# 1. Persistent Top Reading Progress Bar with character symbol and theme colors
# 2. Crisp pixelated SVG mouse cursor (ZERO PNG cursors)
# 3. Dynamic character symbol hover badge
# 4. Removes legacy floating pill and PNG cursor icons

import os
import re
from character_symbols import HUB_HERO_META

base_dir = r"C:\Users\Babitha Ravindra\.gemini\antigravity\scratch\algo-vengers"

for filename, meta in HUB_HERO_META.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: not found.")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    symbol = meta["symbol"]
    symbol_name = meta["symbol_name"]
    hero_color = meta["hero_color"]
    badge_bg = meta["badge_bg"]
    progress_gradient = meta["progress_gradient"]
    title = meta["title"]

    # 1. Clean out legacy floating progress pill or cursor icons
    content = re.sub(r'<div class="reading-progress-pill".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="reading-progress-pill".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="hero-cursor-icon".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="global-top-progress".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="hero-symbol-cursor-badge".*?</div>', '', content, flags=re.DOTALL)

    # 2. Inject CSS into <style>
    custom_css = f"""
    /* Persistent Top Reading Progress Bar & Retro Pixel Cursor */
    html, body {{
      cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath fill='%230f172a' stroke='%23ffffff' stroke-width='1.5' shape-rendering='crispEdges' d='M2 2v18l5-5 4 8 3-1.5-4-8h6L2 2z'/%3E%3C/svg%3E"), auto !important;
    }}
    a, button, .pixel-btn, .topic-card, .mission-card, input, select, label, [role="button"], [data-hero-cursor] {{
      cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath fill='%23dc2626' stroke='%23ffffff' stroke-width='1.5' shape-rendering='crispEdges' d='M2 2v18l5-5 4 8 3-1.5-4-8h6L2 2z'/%3E%3C/svg%3E"), pointer !important;
    }}
    #global-top-progress {{
      position: fixed; top: 0; left: 0; width: 100%; height: 32px;
      background: #0f172a; border-bottom: 2px solid #000; z-index: 10002;
      display: flex; align-items: center; justify-content: space-between; padding: 0 16px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    }}
    .top-progress-hero-badge {{ display: flex; align-items: center; gap: 8px; flex-shrink: 0; }}
    .top-hero-symbol-box {{
      width: 22px; height: 22px; background: {badge_bg}; color: {hero_color};
      border: 1.5px solid {hero_color}; font-family: 'Press Start 2P', monospace; font-size: 0.75rem;
      display: flex; align-items: center; justify-content: center; border-radius: 2px;
    }}
    .top-hero-title {{ font-family: 'Press Start 2P', monospace; font-size: 0.58rem; color: #f8fafc; letter-spacing: 0.5px; }}
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
      font-family: 'Press Start 2P', monospace; font-size: 0.65rem; color: {hero_color};
      box-shadow: 0 0 10px {hero_color}; pointer-events: none; transition: left 0.08s ease-out;
    }}
    .top-progress-percent-readout {{
      font-family: 'Press Start 2P', monospace; font-size: 0.65rem; color: #facc15; min-width: 50px; text-align: right; flex-shrink: 0;
    }}
    .pixel-navbar {{ top: 32px !important; }}
    main {{ padding-top: calc(var(--nav-height, 72px) + 32px + 24px) !important; }}
    #hero-symbol-cursor-badge {{
      position: fixed; pointer-events: none; z-index: 100000; display: none;
      transform: translate(14px, 14px); background: #0f172a; color: {hero_color};
      border: 1.5px solid {hero_color}; font-family: 'Press Start 2P', monospace; font-size: 0.65rem;
      padding: 2px 6px; border-radius: 2px; box-shadow: 0 2px 6px rgba(0,0,0,0.5); font-weight: bold;
    }}
"""

    if "</style>" in content:
        content = content.replace("</style>", f"{custom_css}\n  </style>")

    # 3. Inject Top Progress Bar immediately after <body>
    top_bar_html = f"""
  <!-- Persistent Top Reading Progress Bar (User Directive 3 & 4) -->
  <div id="global-top-progress">
    <div class="top-progress-hero-badge">
      <div class="top-hero-symbol-box">[{symbol}]</div>
      <div class="top-hero-title">{title}</div>
    </div>
    <div class="top-progress-track-wrapper" id="global-progress-track" title="Click anywhere along the bar to jump">
      <div class="top-progress-fill-bar" id="global-progress-fill"></div>
      <div class="top-progress-slider-marker" id="global-progress-marker">{symbol}</div>
    </div>
    <div class="top-progress-percent-readout" id="global-progress-pct">0%</div>
  </div>

  <!-- Character Symbol Cursor Badge (User Directive 1 & 2 - NO PNG CURSOR) -->
  <div id="hero-symbol-cursor-badge">[{symbol}]</div>
"""

    content = re.sub(r'<body[^>]*>', r'\g<0>\n' + top_bar_html, content, count=1)

    # 4. Inject JS handler before </body>
    top_bar_js = f"""
  <script>
    // Top Reading Progress Tracking
    const topFillBar = document.getElementById('global-progress-fill');
    const topMarker = document.getElementById('global-progress-marker');
    const topPct = document.getElementById('global-progress-pct');
    const topTrack = document.getElementById('global-progress-track');

    function updateTopProgress() {{
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? Math.min(100, Math.max(0, Math.round((scrollTop / docHeight) * 100))) : 0;
      if (topFillBar) topFillBar.style.width = pct + '%';
      if (topPct) topPct.textContent = pct + '%';
      if (topMarker) topMarker.style.left = pct + '%';
    }}
    window.addEventListener('scroll', updateTopProgress, {{ passive: true }});
    updateTopProgress();

    topTrack?.addEventListener('click', (e) => {{
      const rect = topTrack.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = Math.max(0, Math.min(1, clickX / rect.width));
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      window.scrollTo({{ top: ratio * docHeight, behavior: 'smooth' }});
    }});

    // Cursor Symbol Hover Badge (NO PNG CURSOR)
    const cursorBadge = document.getElementById('hero-symbol-cursor-badge');
    let pX = -100, pY = -100;
    window.addEventListener('pointermove', (e) => {{
      pX = e.clientX;
      pY = e.clientY;
      if (cursorBadge) {{
        cursorBadge.style.left = pX + 'px';
        cursorBadge.style.top = pY + 'px';
      }}
    }}, {{ passive: true }});

    const hubInteractive = 'a, button, .pixel-btn, .topic-card, .mission-card, input, select, label, .top-progress-track-wrapper, [role="button"], [data-hero-cursor]';
    document.addEventListener('mouseover', (e) => {{
      if (e.target.closest(hubInteractive)) {{
        if (cursorBadge) cursorBadge.style.display = 'block';
      }}
    }});
    document.addEventListener('mouseout', (e) => {{
      if (!e.relatedTarget || !e.relatedTarget.closest(hubInteractive)) {{
        if (cursorBadge) cursorBadge.style.display = 'none';
      }}
    }});
  </script>
"""
    if "</body>" in content:
        content = content.replace("</body>", f"{top_bar_js}\n</body>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated hub page: {filename}")

print("All 7 Hub pages successfully updated with persistent top reading bar and character symbols!")
