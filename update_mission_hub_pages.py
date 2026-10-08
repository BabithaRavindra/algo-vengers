# update_mission_hub_pages.py
import re
from cursor_emblems import CURSOR_URLS

MISSION_CONFIGS = {
    "mission-01.html": {
        "lead_hero": "captain",
        "topic_cursors": {
            "antman": CURSOR_URLS["antman"],
            "drstrange": CURSOR_URLS["doctorstrange"],
            "doctorstrange": CURSOR_URLS["doctorstrange"],
            "vision": CURSOR_URLS["vision"]
        }
    },
    "mission-02.html": {
        "lead_hero": "hulk",
        "topic_cursors": {
            "captain": CURSOR_URLS["captain"],
            "hulk": CURSOR_URLS["hulk"],
            "groot": CURSOR_URLS["groot"],
            "ironman": CURSOR_URLS["ironman"],
            "wanda": CURSOR_URLS["scarletwitch"],
            "scarletwitch": CURSOR_URLS["scarletwitch"]
        }
    },
    "mission-03.html": {
        "lead_hero": "ironman",
        "topic_cursors": {
            "hawkeye": CURSOR_URLS["hawkeye"],
            "spiderman": CURSOR_URLS["spiderman"],
            "warmachine": CURSOR_URLS["warmachine"],
            "quicksilver": CURSOR_URLS["quicksilver"]
        }
    },
    "mission-04.html": {
        "lead_hero": "thor",
        "topic_cursors": {
            "panther": CURSOR_URLS["blackpanther"],
            "blackpanther": CURSOR_URLS["blackpanther"],
            "rocket": CURSOR_URLS["rocket"],
            "thor": CURSOR_URLS["thor"],
            "wolverine": CURSOR_URLS["wolverine"],
            "marvel": CURSOR_URLS["captainmarvel"],
            "captainmarvel": CURSOR_URLS["captainmarvel"]
        }
    },
    "mission-05.html": {
        "lead_hero": "widow",
        "topic_cursors": {
            "widow": CURSOR_URLS["widow"],
            "loki": CURSOR_URLS["loki"]
        }
    }
}

def update_mission_page(filename, config):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove #custom-cursor-follower styles and #hero-symbol-cursor-badge styles
    html = re.sub(r'/\* Custom Cursor Follower \*/\s*#custom-cursor-follower\s*\{[^}]*\}\s*#custom-cursor-follower\.visible\s*\{[^}]*\}\s*@media[^{]*\{[^{]*#custom-cursor-follower\s*\{[^}]*\}\s*\}', '', html)
    html = re.sub(r'#custom-cursor-follower\s*\{[^}]*\}\s*#custom-cursor-follower\.visible\s*\{[^}]*\}\s*@media[^{]*\{[^{]*#custom-cursor-follower\s*\{[^}]*\}\s*\}', '', html)
    html = re.sub(r'#hero-symbol-cursor-badge\s*\{[^}]*\}', '', html)

    # 2. Build Native CSS Cursors
    lead_cursor = CURSOR_URLS[config["lead_hero"]]
    arrow_cursor = CURSOR_URLS["arrow"]

    css_rules = [
        "\n    /* ========================================================================",
        "       NATIVE CSS HARDWARE-ACCELERATED HERO EMBLEM CURSORS (ZERO TRAILING)",
        "       ======================================================================== */",
        f"    html, body {{ cursor: {arrow_cursor} !important; }}",
        f"    a, button, .pixel-btn, input, select, label, .top-progress-track-wrapper, [role=\"button\"] {{ cursor: {lead_cursor} !important; }}"
    ]

    for key, c_url in config["topic_cursors"].items():
        css_rules.append(
            f"    [data-hero-cursor=\"{key}\"], [data-hero-cursor=\"{key}\"] *, .topic-{key}, .topic-{key} * {{ cursor: {c_url} !important; }}"
        )

    native_css_block = "\n".join(css_rules) + "\n"

    # Insert before </style>
    if "NATIVE CSS HARDWARE-ACCELERATED HERO EMBLEM CURSORS" not in html:
        html = html.replace("</style>", native_css_block + "  </style>")
    else:
        # replace existing block
        html = re.sub(r'/\* ========================================================================\s*NATIVE CSS HARDWARE-ACCELERATED HERO EMBLEM CURSORS.*?</style>', native_css_block + "  </style>", html, flags=re.DOTALL)

    # 3. Remove trailing div <div id="hero-symbol-cursor-badge">...</div>
    html = re.sub(r'<!-- Character Symbol Cursor Badge [^>]*-->\s*<div id="hero-symbol-cursor-badge"[^>]*>[^<]*</div>', '', html)
    html = re.sub(r'<div id="hero-symbol-cursor-badge"[^>]*>[^<]*</div>', '', html)
    html = re.sub(r'<div id="custom-cursor-follower"[^>]*>.*?</div>\s*</div>', '', html, flags=re.DOTALL)

    # 4. Clean bottom from </main> to </body>
    main_end_idx = html.find('</main>')
    if main_end_idx != -1:
        prefix = html[:main_end_idx + len('</main>')]
        clean_bottom = """

  <script>
    /* Audio Synthesizer */
    class HubRetroAudio {
      constructor() { this.ctx = null; }
      init() {
        if (!this.ctx && typeof (window.AudioContext || window.webkitAudioContext) !== 'undefined') {
          const AudioContextClass = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContextClass();
        }
        if (this.ctx && this.ctx.state === 'suspended') this.ctx.resume();
      }
      playHover() {
        this.init(); if (!this.ctx) return;
        try {
          const osc = this.ctx.createOscillator(); const gain = this.ctx.createGain();
          osc.type = 'sine'; osc.frequency.setValueAtTime(520, this.ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(760, this.ctx.currentTime + 0.04);
          gain.gain.setValueAtTime(0.04, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
          osc.connect(gain); gain.connect(this.ctx.destination);
          osc.start(); osc.stop(this.ctx.currentTime + 0.04);
        } catch(e) {}
      }
      playClick() {
        this.init(); if (!this.ctx) return;
        try {
          const osc = this.ctx.createOscillator(); const gain = this.ctx.createGain();
          osc.type = 'triangle'; osc.frequency.setValueAtTime(320, this.ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(140, this.ctx.currentTime + 0.04);
          gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
          osc.connect(gain); gain.connect(this.ctx.destination);
          osc.start(); osc.stop(this.ctx.currentTime + 0.04);
        } catch(e) {}
      }
    }
    const hubAudio = new HubRetroAudio();

    // Top Reading Progress Tracking
    const topFillBar = document.getElementById('global-progress-fill');
    const topMarker = document.getElementById('global-progress-marker');
    const topPct = document.getElementById('global-progress-pct');
    const topTrack = document.getElementById('global-progress-track');

    function updateTopProgress() {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? Math.min(100, Math.max(0, Math.round((scrollTop / docHeight) * 100))) : 0;
      if (topFillBar) topFillBar.style.width = pct + '%';
      if (topPct) topPct.textContent = pct + '%';
      if (topMarker) topMarker.style.left = pct + '%';
    }
    window.addEventListener('scroll', updateTopProgress, { passive: true });
    updateTopProgress();

    topTrack?.addEventListener('click', (e) => {
      const rect = topTrack.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const ratio = Math.max(0, Math.min(1, clickX / rect.width));
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      window.scrollTo({ top: ratio * docHeight, behavior: 'smooth' });
    });

    // Sound feedback on interactive controls
    const hubInteractive = 'a, button, .pixel-btn, .topic-card, .mission-card, input, select, label, .top-progress-track-wrapper, [role="button"], [data-hero-cursor]';
    document.addEventListener('mouseover', (e) => {
      if (e.target.closest(hubInteractive)) {
        hubAudio.playHover();
      }
    });
    document.addEventListener('click', (e) => {
      if (e.target.closest(hubInteractive)) {
        hubAudio.playClick();
      }
    });
  </script>
</body>
</html>
"""
        html = prefix + clean_bottom

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filename} successfully.")

if __name__ == '__main__':
    for fname, cfg in MISSION_CONFIGS.items():
        update_mission_page(fname, cfg)
