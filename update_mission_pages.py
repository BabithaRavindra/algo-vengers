import re
import os

print("Updating missions.html and mission hub subpages...")

# 1. UPDATE missions.html
with open("missions.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add CSS for .tile-sprite img, .pixel-sprite-img, .cursor-icon-wrapper img
tile_img_css = """
    .tile-sprite img,
    .pixel-sprite-img {
      max-width: 110px;
      max-height: 125px;
      width: auto;
      height: auto;
      object-fit: contain;
      image-rendering: pixelated;
      image-rendering: crisp-edges;
      filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.25));
      transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .mission-tile:hover .pixel-sprite-img {
      transform: scale(1.12) translateY(-4px);
    }
    .cursor-icon-wrapper img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      image-rendering: pixelated;
      image-rendering: crisp-edges;
    }
"""
if ".pixel-sprite-img" not in content:
    content = content.replace(".tile-sprite svg {", tile_img_css + "\n    .tile-sprite svg {")

# Replace SVG in the 5 cards in missions.html
# Mission 01: Captain America
content = re.sub(
    r'(<!-- Captain America Dominant Visual Shield & Figure -->\s*<div class="tile-character-display">\s*<div class="tile-character-aura"></div>\s*<div class="tile-sprite">)\s*<svg.*?</svg>(\s*</div>\s*</div>)',
    r'\1<img src="assets/captainamerica.png" class="pixel-sprite-img" alt="Captain America">\2',
    content, flags=re.DOTALL
)

# Mission 02: Hulk
content = re.sub(
    r'(<!-- Hulk Dominant Visual Fist & Figure -->\s*<div class="tile-character-display">\s*<div class="tile-character-aura"></div>\s*<div class="tile-sprite">)\s*<svg.*?</svg>(\s*</div>\s*</div>)',
    r'\1<img src="assets/hulk.png" class="pixel-sprite-img" alt="Hulk">\2',
    content, flags=re.DOTALL
)

# Mission 03: Iron Man
content = re.sub(
    r'(<!-- Iron Man Dominant Visual Helmet & Scanning HUD -->\s*<div class="tile-character-display">\s*<div class="tile-character-aura"></div>\s*<div class="tile-sprite">)\s*<svg.*?</svg>(\s*</div>\s*</div>)',
    r'\1<img src="assets/ironman.png" class="pixel-sprite-img" alt="Iron Man">\2',
    content, flags=re.DOTALL
)

# Mission 04: Thor
content = re.sub(
    r'(<!-- Thor Dominant Visual Figure & Mjolnir with Lightning -->\s*<div class="tile-character-display">\s*<div class="tile-character-aura"></div>\s*<div class="tile-sprite">)\s*<svg.*?</svg>(\s*</div>\s*</div>)',
    r'\1<img src="assets/thor.png" class="pixel-sprite-img" alt="Thor">\2',
    content, flags=re.DOTALL
)

# Mission 05: Black Widow
content = re.sub(
    r'(<!-- Black Widow Dominant Visual Tactical Icon & Figure -->\s*<div class="tile-character-display">\s*<div class="tile-character-aura"></div>\s*<div class="tile-sprite">)\s*<svg.*?</svg>(\s*</div>\s*</div>)',
    r'\1<img src="assets/blackwidow.png" class="pixel-sprite-img" alt="Black Widow">\2',
    content, flags=re.DOTALL
)

# Replace cursorTemplates in HeroCursorManager
old_cursor_block = re.search(r'this\.cursorTemplates\s*=\s*\{.*?\};', content, flags=re.DOTALL)
if old_cursor_block:
    new_cursor_block = """this.cursorTemplates = {
          captain: `<img src="assets/captainamerica.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
          hulk: `<img src="assets/hulk.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
          ironman: `<img src="assets/ironman.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
          thor: `<img src="assets/thor.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
          widow: `<img src="assets/blackwidow.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`
        };"""
    content = content.replace(old_cursor_block.group(0), new_cursor_block)

with open("missions.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated missions.html!")

# 2. UPDATE mission-01.html
with open("mission-01.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update templates in mission-01
m1_templates = """const templates = {
      antman: `<img src="assets/antman.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      drstrange: `<img src="assets/doctorstrange.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      vision: `<img src="assets/vision.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`
    };"""
content = re.sub(r'const templates\s*=\s*\{.*?\};', m1_templates, content, flags=re.DOTALL)

with open("mission-01.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated mission-01.html!")

# 3. UPDATE mission-02.html
with open("mission-02.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add .topic-hulk styles
if ".topic-hulk" not in content:
    content = content.replace(".topic-falcon .char-aura {", """.topic-hulk .char-aura { background: #16a34a; }
    .topic-hulk:hover { background: #f0fdf4; border-color: #16a34a; }
    .topic-hulk .card-btn { background: #16a34a; color: #fff; }
    .topic-falcon .char-aura {""")

# Card 2: Queues (Update to Hulk)
content = re.sub(
    r'<!-- TOPIC 02: QUEUES \(FALCON\).*?<!-- TOPIC 03: TREES',
    """<!-- TOPIC 02: QUEUES (HULK) -->
          <a href="topic-queues.html" class="topic-card topic-hulk" data-hero-cursor="hulk">
            <div class="card-top">
              <span class="card-num">TOPIC 02</span>
              <span class="card-hero-badge">HULK</span>
            </div>
            <div class="character-display">
              <div class="char-aura"></div>
              <div class="char-sprite"><img src="assets/hulk.png" class="pixel-sprite-img" alt="Hulk"></div>
            </div>
            <div class="card-body">
              <h2 class="card-title">QUEUES</h2>
              <p class="card-desc">First-In-First-Out (FIFO) queue buffer: Hulk powers through ordered scheduling.</p>
              <div class="complexity-pill">Enqueue/Dequeue: O(1)</div>
            </div>
            <span class="pixel-btn card-btn">ACCESS TOPIC</span>
          </a>

        </div>

        <!-- ROW 2 (2 CARDS CENTERED) -->
        <!-- TOPIC 03: TREES""",
    content, flags=re.DOTALL
)

# Card 3: Trees (Groot)
content = re.sub(
    r'(<!-- TOPIC 03: TREES.*?<div class="char-sprite">)\s*<svg.*?</svg>(\s*</div>)',
    r'\1<img src="assets/groot.png" class="pixel-sprite-img" alt="Groot">\2',
    content, flags=re.DOTALL
)

# Card 4: Dictionaries (Iron Man)
content = re.sub(
    r'(<!-- TOPIC 04: DICTIONARIES.*?<div class="char-sprite">)\s*<svg.*?</svg>(\s*</div>)',
    r'\1<img src="assets/ironman.png" class="pixel-sprite-img" alt="Iron Man">\2',
    content, flags=re.DOTALL
)

# Card 5: Sets (Scarlet Witch)
content = re.sub(
    r'(<!-- TOPIC 05: SETS.*?<div class="char-sprite">)\s*<svg.*?</svg>(\s*</div>)',
    r'\1<img src="assets/scarletwitch.png" class="pixel-sprite-img" alt="Scarlet Witch">\2',
    content, flags=re.DOTALL
)

# Cursor templates in mission-02
m2_templates = """const templates = {
      captain: `<img src="assets/captainamerica.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      hulk: `<img src="assets/hulk.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      falcon: `<img src="assets/hulk.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      groot: `<img src="assets/groot.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      ironman: `<img src="assets/ironman.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      wanda: `<img src="assets/scarletwitch.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`
    };"""
content = re.sub(r'const templates\s*=\s*\{.*?\};', m2_templates, content, flags=re.DOTALL)

with open("mission-02.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated mission-02.html!")

# 4. UPDATE mission-03.html
with open("mission-03.html", "r", encoding="utf-8") as f:
    content = f.read()

m3_templates = """const templates = {
      hawkeye: `<img src="assets/hawkeye.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      spiderman: `<img src="assets/spiderman.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      warmachine: `<img src="assets/warmachine.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      quicksilver: `<img src="assets/quicksilver.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`
    };"""
content = re.sub(r'const templates\s*=\s*\{.*?\};', m3_templates, content, flags=re.DOTALL)

with open("mission-03.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated mission-03.html!")

# 5. UPDATE mission-04.html
with open("mission-04.html", "r", encoding="utf-8") as f:
    content = f.read()

m4_templates = """const templates = {
      panther: `<img src="assets/blackpanther.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      rocket: `<img src="assets/rocket.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      thor: `<img src="assets/thor.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      wolverine: `<img src="assets/wolverine.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      marvel: `<img src="assets/captainmarvel.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`
    };"""
content = re.sub(r'const templates\s*=\s*\{.*?\};', m4_templates, content, flags=re.DOTALL)

with open("mission-04.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated mission-04.html!")

# 6. UPDATE mission-05.html
with open("mission-05.html", "r", encoding="utf-8") as f:
    content = f.read()

m5_templates = """const templates = {
      loki: `<img src="assets/loki.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`,
      widow: `<img src="assets/blackwidow.png" style="width:34px;height:34px;object-fit:contain;image-rendering:pixelated;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.4));">`
    };"""
content = re.sub(r'const templates\s*=\s*\{.*?\};', m5_templates, content, flags=re.DOTALL)

with open("mission-05.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated mission-05.html!")
