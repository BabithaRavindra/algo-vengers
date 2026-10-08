# update_index_page.py
import re
from cursor_emblems import CURSOR_URLS

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove #custom-cursor-follower styles and old fallback cursor rules (lines ~535-592)
    old_cursor_engine = re.compile(
        r'/\* ========================================================================\s*CUSTOM PIXEL CURSOR ENGINE.*?'
        r'/\* ========================================================================\s*CHARACTER STAGES',
        re.DOTALL
    )
    html = old_cursor_engine.sub(
        '/* ========================================================================\n       CHARACTER STAGES',
        html
    )

    # 2. Remove #hero-cursor-icon styles (lines ~1557-1565)
    html = re.sub(r'#hero-cursor-icon\s*\{[^}]*\}\s*#hero-cursor-icon\.active\s*\{[^}]*\}\s*#hero-cursor-icon img\s*\{[^}]*\}', '', html)

    # 3. Remove #hero-symbol-cursor-badge styles
    html = re.sub(r'#hero-symbol-cursor-badge\s*\{[^}]*\}', '', html)

    # 4. Remove old cursor definitions around line 1568-1573
    old_top_cursor = re.compile(
        r'/\* Persistent Top Reading Progress Bar & Retro Pixel Cursor \*/\s*html, body \{.*?\}'
        r'\s*a, button, \.pixel-btn, \.topic-card, \.mission-card, input, select, label, \[role="button"\], \[data-hero-cursor\] \{.*?\}',
        re.DOTALL
    )
    html = old_top_cursor.sub('/* Persistent Top Reading Progress Bar */', html)

    # 5. Build Native CSS Cursors
    shield_cursor = CURSOR_URLS["shield"]
    arrow_cursor = CURSOR_URLS["arrow"]
    cap_cursor = CURSOR_URLS["captain"]
    hulk_cursor = CURSOR_URLS["hulk"]
    iron_cursor = CURSOR_URLS["ironman"]
    thor_cursor = CURSOR_URLS["thor"]
    widow_cursor = CURSOR_URLS["widow"]
    hawkeye_cursor = CURSOR_URLS["hawkeye"]
    spidey_cursor = CURSOR_URLS["spiderman"]

    native_css = f"""
    /* ========================================================================
       NATIVE CSS HARDWARE-ACCELERATED HERO EMBLEM CURSORS (ZERO TRAILING)
       ======================================================================== */
    html, body {{
      cursor: {arrow_cursor} !important;
    }}

    /* General interactive elements: S.H.I.E.L.D. Division Emblem */
    a, button, .pixel-btn, .topic-card, .mission-card, .arsenal-card, .algo-hero-card, input, select, label, .reading-progress-track, .top-progress-track-wrapper, [role="button"] {{
      cursor: {shield_cursor} !important;
    }}

    /* Homepage Mission Cards */
    [data-access-mission="mission-01"], [data-access-mission="mission-01"] * {{
      cursor: {cap_cursor} !important;
    }}
    [data-access-mission="mission-02"], [data-access-mission="mission-02"] * {{
      cursor: {hulk_cursor} !important;
    }}
    [data-access-mission="mission-03"], [data-access-mission="mission-03"] * {{
      cursor: {iron_cursor} !important;
    }}
    [data-access-mission="mission-04"], [data-access-mission="mission-04"] * {{
      cursor: {thor_cursor} !important;
    }}
    [data-access-mission="mission-05"], [data-access-mission="mission-05"] * {{
      cursor: {widow_cursor} !important;
    }}

    /* Hero Themed Sections */
    [data-hero-cursor="ironman"] a, [data-hero-cursor="ironman"] button, [data-hero-cursor="ironman"] .pixel-btn, [data-hero-cursor="ironman"] .arsenal-card, [data-hero-cursor="ironman"] .algo-hero-card {{
      cursor: {iron_cursor} !important;
    }}
    [data-hero-cursor="captain"] a, [data-hero-cursor="captain"] button, [data-hero-cursor="captain"] .pixel-btn, [data-hero-cursor="captain"] .mission-card, [data-hero-cursor="captain"] .arsenal-card, [data-hero-cursor="captain"] .algo-hero-card {{
      cursor: {cap_cursor} !important;
    }}
    [data-hero-cursor="thor"] a, [data-hero-cursor="thor"] button, [data-hero-cursor="thor"] .pixel-btn, [data-hero-cursor="thor"] .mission-card, [data-hero-cursor="thor"] .arsenal-card, [data-hero-cursor="thor"] .algo-hero-card {{
      cursor: {thor_cursor} !important;
    }}
    [data-hero-cursor="hulk"] a, [data-hero-cursor="hulk"] button, [data-hero-cursor="hulk"] .pixel-btn, [data-hero-cursor="hulk"] .mission-card, [data-hero-cursor="hulk"] .arsenal-card, [data-hero-cursor="hulk"] .algo-hero-card {{
      cursor: {hulk_cursor} !important;
    }}
    [data-hero-cursor="widow"] a, [data-hero-cursor="widow"] button, [data-hero-cursor="widow"] .pixel-btn, [data-hero-cursor="widow"] .mission-card, [data-hero-cursor="widow"] .arsenal-card, [data-hero-cursor="widow"] .algo-hero-card {{
      cursor: {widow_cursor} !important;
    }}
    [data-hero-cursor="hawkeye"] a, [data-hero-cursor="hawkeye"] button, [data-hero-cursor="hawkeye"] .pixel-btn, [data-hero-cursor="hawkeye"] .mission-card, [data-hero-cursor="hawkeye"] .arsenal-card, [data-hero-cursor="hawkeye"] .algo-hero-card {{
      cursor: {hawkeye_cursor} !important;
    }}
    [data-hero-cursor="spiderman"] a, [data-hero-cursor="spiderman"] button, [data-hero-cursor="spiderman"] .pixel-btn, [data-hero-cursor="spiderman"] .mission-card, [data-hero-cursor="spiderman"] .arsenal-card, [data-hero-cursor="spiderman"] .algo-hero-card {{
      cursor: {spidey_cursor} !important;
    }}
"""
    html = html.replace("</style>", native_css + "\n  </style>")

    # 6. Remove <div id="hero-symbol-cursor-badge">[★]</div>
    html = re.sub(r'<!-- Character Symbol Cursor Badge [^>]*-->\s*<div id="hero-symbol-cursor-badge"[^>]*>[^<]*</div>', '', html)
    html = re.sub(r'<div id="hero-symbol-cursor-badge"[^>]*>[^<]*</div>', '', html)

    # 7. Remove class HeroCursorManager
    hero_cursor_mgr = re.compile(
        r'/\* ======================================================================\s*4\. CUSTOM PIXEL CURSOR FOLLOWER & TRANSFORMER\s*====================================================================== \*/'
        r'.*?/\* ======================================================================\s*5\. MISSION DOSSIER MODAL CONTROLLER',
        re.DOTALL
    )
    html = hero_cursor_mgr.sub(
        '/* ======================================================================\n       5. MISSION DOSSIER MODAL CONTROLLER',
        html
    )

    # 8. Remove new HeroCursorManager(); in DOMContentLoaded
    html = html.replace("new HeroCursorManager();\n", "")
    html = html.replace("new HeroCursorManager();", "")

    # 9. Clean up trailing cursorBadge script before </body>
    trailing_badge_script = re.compile(
        r'// Cursor Symbol Hover Badge \(NO PNG CURSOR\)\s*const cursorBadge = document\.getElementById\(\'hero-symbol-cursor-badge\'\);.*?window\.scrollTo\(\{ top: ratio \* docHeight, behavior: \'smooth\' \}\);\s*\}\);',
        re.DOTALL
    )
    # Note: in index.html, cursorBadge comes AFTER topTrack?.addEventListener('click'...)
    # Let's inspect that part:
    old_end_script = re.compile(
        r'// Cursor Symbol Hover Badge \(NO PNG CURSOR\).*?if \(!e\.relatedTarget \|\| !e\.relatedTarget\.closest\(hubInteractive\)\) \{\s*if \(cursorBadge\) cursorBadge\.style\.display = \'none\';\s*\}\s*\}\);',
        re.DOTALL
    )
    html = old_end_script.sub('', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html successfully.")

if __name__ == '__main__':
    update_index()
