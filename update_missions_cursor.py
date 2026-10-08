# update_missions_cursor.py - Replaces trailing cursor in missions.html with native CSS circular emblem cursors
import re
from cursor_emblems import CURSOR_URLS

with open("missions.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove HeroCursorManager class and its instantiation
content = re.sub(r'/\* 3\. Hero Custom Cursor Follower \*/.*?class HeroCursorManager.*?\}\s*\}', '', content, flags=re.DOTALL)
content = re.sub(r'new HeroCursorManager\(\);\s*', '', content)

# 2. Remove any custom-cursor-follower DOM elements or CSS
content = re.sub(r'#custom-cursor-follower\s*\{[^}]*\}', '', content)
content = re.sub(r'#custom-cursor-follower\.visible\s*\{[^}]*\}', '', content)
content = re.sub(r'#custom-cursor-follower\.clicking\s*\{[^}]*\}', '', content)
content = re.sub(r'\.cursor-icon-wrapper\s*\{[^}]*\}', '', content)
content = re.sub(r'\.cursor-icon-wrapper svg\s*\{[^}]*\}', '', content)
content = re.sub(r'@media[^{]*\{[^{]*#custom-cursor-follower[^}]*\}[^}]*\}', '', content)
content = re.sub(r'<div id="hero-symbol-cursor-badge".*?</div>', '', content)

# 3. Build native CSS rules
native_cursor_css = f"""
    /* ========================================================================
       NATIVE CSS HARDWARE-ACCELERATED HERO EMBLEM CURSORS (ZERO TRAILING)
       ======================================================================== */
    html, body {{
      cursor: {CURSOR_URLS['arrow']} !important;
    }}

    /* Default interactive elements: S.H.I.E.L.D. circular emblem */
    a, button, .pixel-btn, [role="button"], input, select, label {{
      cursor: {CURSOR_URLS['shield']} !important;
    }}

    /* Mission 01: Captain America Blue Circle with Shield */
    .tile-m1, .tile-m1 *, [data-hero-cursor="captain"], [data-hero-cursor="captain"] * {{
      cursor: {CURSOR_URLS['captain']} !important;
    }}

    /* Mission 02: Hulk Green Circle with Clenched Gamma Fist */
    .tile-m2, .tile-m2 *, [data-hero-cursor="hulk"], [data-hero-cursor="hulk"] * {{
      cursor: {CURSOR_URLS['hulk']} !important;
    }}

    /* Mission 03: Iron Man Red Circle with Glowing Arc Reactor */
    .tile-m3, .tile-m3 *, [data-hero-cursor="ironman"], [data-hero-cursor="ironman"] * {{
      cursor: {CURSOR_URLS['ironman']} !important;
    }}

    /* Mission 04: Thor Circle with Mjolnir Hammer */
    .tile-m4, .tile-m4 *, [data-hero-cursor="thor"], [data-hero-cursor="thor"] * {{
      cursor: {CURSOR_URLS['thor']} !important;
    }}

    /* Mission 05: Black Widow Black Circle with Red Sand Clock */
    .tile-m5, .tile-m5 *, [data-hero-cursor="widow"], [data-hero-cursor="widow"] * {{
      cursor: {CURSOR_URLS['widow']} !important;
    }}
"""

# Replace or inject into style
if "</style>" in content:
    content = content.replace("</style>", f"{native_cursor_css}\n  </style>")

with open("missions.html", "w", encoding="utf-8") as f:
    f.write(content)

print("missions.html successfully updated with native CSS circular emblem cursors!")
