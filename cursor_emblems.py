# cursor_emblems.py - Authentic Marvel Hero Circular Emblems as Native CSS Cursors
# ZERO trailing divs, ZERO PNG cursor images.
# Pure hardware-accelerated CSS cursor: url("data:image/svg+xml,...") 16 16, pointer !important;

import urllib.parse

def make_cursor_url(svg_content):
    # Compact and URL-encode SVG for CSS cursor
    clean_svg = " ".join(svg_content.strip().split())
    encoded = urllib.parse.quote(clean_svg)
    return f"url(\"data:image/svg+xml,{encoded}\") 16 16, pointer"

EMBLEM_SVGS = {
    # Captain America: Blue circle with Vibranium Shield & Star
    "captain": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#dc2626" stroke="#0f172a" stroke-width="1.5"/>
      <circle cx="16" cy="16" r="11" fill="#ffffff" stroke="#0f172a" stroke-width="1"/>
      <circle cx="16" cy="16" r="8" fill="#dc2626"/>
      <circle cx="16" cy="16" r="5" fill="#2563eb"/>
      <polygon points="16,12 17.5,15.5 21,15.5 18,17.5 19.5,21 16,18.8 12.5,21 14,17.5 11,15.5 14.5,15.5" fill="#ffffff"/>
    </svg>""",

    # Thor: Circle with Mjolnir Hammer & Storm Lightning
    "thor": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#1e293b" stroke="#ca8a04" stroke-width="2"/>
      <rect x="9" y="8" width="14" height="9" fill="#94a3b8" stroke="#000" stroke-width="1.5"/>
      <rect x="11" y="10" width="10" height="2" fill="#f8fafc"/>
      <rect x="14" y="17" width="4" height="9" fill="#78350f" stroke="#000" stroke-width="1"/>
      <path d="M16 9 L14 13 L17 13 L15 17" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
    </svg>""",

    # Black Widow: Black Circle with Red Sand Clock / Hourglass
    "widow": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#0f172a" stroke="#e11d48" stroke-width="2"/>
      <polygon points="10,9 22,9 16,16" fill="#dc2626"/>
      <polygon points="16,16 22,23 10,23" fill="#dc2626"/>
      <circle cx="16" cy="16" r="1.5" fill="#ffffff"/>
      <circle cx="16" cy="16" r="14" fill="none" stroke="#000" stroke-width="1"/>
    </svg>""",

    # Iron Man: Red Circle with Glowing Arc Reactor
    "ironman": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#991b1b" stroke="#facc15" stroke-width="2"/>
      <circle cx="16" cy="16" r="9" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="16" cy="16" r="5" fill="#38bdf8"/>
      <circle cx="16" cy="16" r="2.5" fill="#ffffff"/>
      <polygon points="16,8 18,13 14,13" fill="#facc15"/>
      <polygon points="16,24 14,19 18,19" fill="#facc15"/>
      <polygon points="8,16 13,14 13,18" fill="#facc15"/>
      <polygon points="24,16 19,18 19,14" fill="#facc15"/>
    </svg>""",

    # Hulk: Green Circle with Clenched Gamma Fist
    "hulk": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#15803d" stroke="#581c87" stroke-width="2"/>
      <rect x="9" y="11" width="14" height="13" rx="2" fill="#22c55e" stroke="#000" stroke-width="1.5"/>
      <rect x="10" y="8" width="3" height="4" fill="#16a34a" stroke="#000" stroke-width="1"/>
      <rect x="13.5" y="7" width="3" height="5" fill="#16a34a" stroke="#000" stroke-width="1"/>
      <rect x="17" y="7" width="3" height="5" fill="#16a34a" stroke="#000" stroke-width="1"/>
      <rect x="20" y="9" width="3" height="4" fill="#16a34a" stroke="#000" stroke-width="1"/>
      <rect x="10" y="21" width="12" height="3" fill="#581c87"/>
    </svg>""",

    # Spider-Man: Red Circle with Spider Emblem
    "spiderman": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#dc2626" stroke="#2563eb" stroke-width="2"/>
      <ellipse cx="16" cy="16" rx="3" ry="5" fill="#0f172a"/>
      <circle cx="16" cy="12" r="2" fill="#0f172a"/>
      <path d="M16 14 Q10 10 7 14 M16 17 Q9 16 8 20 M16 14 Q22 10 25 14 M16 17 Q23 16 24 20" stroke="#0f172a" stroke-width="1.5" fill="none"/>
      <line x1="16" y1="2" x2="16" y2="10" stroke="#f8fafc" stroke-width="1"/>
    </svg>""",

    # Doctor Strange: Mystic Circle with Eye of Agamotto
    "doctorstrange": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#7e22ce" stroke="#f59e0b" stroke-width="2"/>
      <circle cx="16" cy="16" r="9" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <ellipse cx="16" cy="16" rx="6" ry="3.5" fill="#f59e0b"/>
      <circle cx="16" cy="16" r="2" fill="#22c55e"/>
    </svg>""",

    # Hawkeye: Purple Circle with Archery Bullseye Target & Arrow
    "hawkeye": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#7c3aed" stroke="#d97706" stroke-width="2"/>
      <circle cx="16" cy="16" r="9" fill="#ffffff"/>
      <circle cx="16" cy="16" r="6" fill="#7c3aed"/>
      <circle cx="16" cy="16" r="3" fill="#facc15"/>
      <line x1="6" y1="26" x2="26" y2="6" stroke="#0f172a" stroke-width="2"/>
      <polygon points="26,6 21,8 24,11" fill="#0f172a"/>
    </svg>""",

    # Groot: Flora Circle with Branch Canopy
    "groot": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#15803d" stroke="#78350f" stroke-width="2"/>
      <path d="M16 26 L16 14 M16 18 L11 12 M16 15 L21 10" stroke="#78350f" stroke-width="2.5" fill="none"/>
      <circle cx="11" cy="12" r="2.5" fill="#22c55e"/>
      <circle cx="21" cy="10" r="2.5" fill="#22c55e"/>
      <circle cx="16" cy="10" r="3" fill="#4ade80"/>
    </svg>""",

    # Ant-Man: Red Circle with Quantum Particle
    "antman": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#ef4444" stroke="#0f172a" stroke-width="2"/>
      <circle cx="16" cy="16" r="4" fill="#ffffff" stroke="#000" stroke-width="1"/>
      <ellipse cx="16" cy="16" rx="10" ry="3" fill="none" stroke="#facc15" stroke-width="1.5" transform="rotate(30 16 16)"/>
      <ellipse cx="16" cy="16" rx="10" ry="3" fill="none" stroke="#facc15" stroke-width="1.5" transform="rotate(-30 16 16)"/>
    </svg>""",

    # Vision: Green Circle with Mind Stone Hexagon
    "vision": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#059669" stroke="#eab308" stroke-width="2"/>
      <polygon points="16,8 23,12 23,20 16,24 9,20 9,12" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
      <polygon points="16,11 20,13.5 20,18.5 16,21 12,18.5 12,13.5" fill="#facc15"/>
    </svg>""",

    # Scarlet Witch: Chaos Red Circle with Hex Spark
    "scarletwitch": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#e11d48" stroke="#831843" stroke-width="2"/>
      <path d="M16 6 L18 13 L25 15 L19 18 L20 25 L16 20 L12 25 L13 18 L7 15 L14 13 Z" fill="#fda4af" stroke="#000" stroke-width="1"/>
      <circle cx="16" cy="16" r="2.5" fill="#ffffff"/>
    </svg>""",

    # War Machine: Steel Circle with Armor Turret
    "warmachine": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#475569" stroke="#0f172a" stroke-width="2"/>
      <rect x="10" y="11" width="12" height="11" fill="#94a3b8" stroke="#000" stroke-width="1.5"/>
      <rect x="14" y="6" width="4" height="6" fill="#0f172a"/>
      <rect x="12" y="14" width="3" height="2" fill="#dc2626"/>
      <rect x="17" y="14" width="3" height="2" fill="#dc2626"/>
    </svg>""",

    # Quicksilver: Cyan Circle with Supersonic Bolt
    "quicksilver": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
      <polygon points="17,6 9,17 15,17 13,26 23,14 17,14" fill="#facc15" stroke="#000" stroke-width="1"/>
    </svg>""",

    # Black Panther: Vibranium Circle with Royal Claws
    "blackpanther": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#0f172a" stroke="#6b21a8" stroke-width="2"/>
      <circle cx="16" cy="16" r="9" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="2,2"/>
      <polygon points="16,19 14,24 18,24" fill="#ffffff"/>
      <polygon points="11,18 9,22 13,22" fill="#ffffff"/>
      <polygon points="21,18 19,22 23,22" fill="#ffffff"/>
    </svg>""",

    # Rocket Raccoon: Amber Circle with Plasma Gear
    "rocket": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#d97706" stroke="#ea580c" stroke-width="2"/>
      <circle cx="16" cy="16" r="8" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
      <circle cx="16" cy="16" r="3" fill="#d97706"/>
      <rect x="15" y="6" width="2" height="3" fill="#facc15"/>
      <rect x="15" y="23" width="2" height="3" fill="#facc15"/>
      <rect x="6" y="15" width="3" height="2" fill="#facc15"/>
      <rect x="23" y="15" width="3" height="2" fill="#facc15"/>
    </svg>""",

    # Wolverine: Yellow Circle with Crossed Adamantium Claws
    "wolverine": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#ca8a04" stroke="#1d4ed8" stroke-width="2"/>
      <path d="M9 24 Q13 14 20 8 M12 25 Q16 15 23 9 M15 26 Q19 16 26 10" stroke="#f8fafc" stroke-width="1.5" fill="none"/>
      <path d="M23 24 Q19 14 12 8 M20 25 Q16 15 9 9 M17 26 Q13 16 6 10" stroke="#94a3b8" stroke-width="1.5" fill="none"/>
    </svg>""",

    # Captain Marvel: Red Circle with Hala 8-Point Cosmic Star
    "captainmarvel": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#dc2626" stroke="#facc15" stroke-width="2"/>
      <polygon points="16,6 18,13 25,10 20,16 25,22 18,19 16,26 14,19 7,22 12,16 7,10 14,13" fill="#facc15" stroke="#000" stroke-width="1"/>
      <circle cx="16" cy="16" r="2.5" fill="#ffffff"/>
    </svg>""",

    # Loki: Emerald Circle with Horned Crown
    "loki": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#15803d" stroke="#ca8a04" stroke-width="2"/>
      <path d="M8 8 Q12 18 16 18 Q20 18 24 8 Q21 16 16 20 Q11 16 8 8 Z" fill="#facc15" stroke="#000" stroke-width="1"/>
      <circle cx="16" cy="20" r="2" fill="#22c55e"/>
    </svg>""",

    # S.H.I.E.L.D. Division Emblem (For Missions Hub & HQ)
    "shield": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" shape-rendering="crispEdges">
      <circle cx="16" cy="16" r="14" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>
      <polygon points="16,8 23,14 20,24 16,22 12,24 9,14" fill="#0284c7" stroke="#ffffff" stroke-width="1"/>
      <polygon points="16,11 20,15 16,19 12,15" fill="#facc15"/>
    </svg>""",

    # Default Pixel Arrow Pointer
    "arrow": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" shape-rendering="crispEdges">
      <path fill="#0f172a" stroke="#ffffff" stroke-width="1.5" d="M2 2v18l5-5 4 8 3-1.5-4-8h6L2 2z"/>
    </svg>"""
}

# Pre-generate CSS cursor URLs
CURSOR_URLS = { k: make_cursor_url(v) for k, v in EMBLEM_SVGS.items() }
CURSOR_URLS["arrow"] = "url(\"data:image/svg+xml," + urllib.parse.quote(" ".join(EMBLEM_SVGS["arrow"].split())) + "\") 0 0, auto"

# Hero Name to Cursor Key map
HERO_CURSOR_KEY_MAP = {
    "ANT-MAN": "antman",
    "DOCTOR STRANGE": "doctorstrange",
    "VISION": "vision",
    "CAPTAIN AMERICA": "captain",
    "HULK": "hulk",
    "GROOT": "groot",
    "IRON MAN": "ironman",
    "SCARLET WITCH": "scarletwitch",
    "HAWKEYE": "hawkeye",
    "SPIDER-MAN": "spiderman",
    "WAR MACHINE": "warmachine",
    "QUICKSILVER": "quicksilver",
    "BLACK PANTHER": "blackpanther",
    "ROCKET RACCOON": "rocket",
    "THOR": "thor",
    "WOLVERINE": "wolverine",
    "CAPTAIN MARVEL": "captainmarvel",
    "LOKI": "loki",
    "BLACK WIDOW": "widow"
}

def get_hero_cursor_url(hero_name):
    key = HERO_CURSOR_KEY_MAP.get(hero_name, "captain")
    return CURSOR_URLS[key]
