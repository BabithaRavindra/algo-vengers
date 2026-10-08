import os
import re

# 1. Update Mission 01
m1_path = "mission-01.html"
if os.path.exists(m1_path):
    with open(m1_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add sprite img css
    if ".pixel-sprite-img" not in content:
        content = content.replace("</style>", """
    .pixel-sprite-img {
      max-width: 100px; max-height: 115px; width: auto; height: auto;
      object-fit: contain; image-rendering: pixelated; image-rendering: crisp-edges;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2)); transition: transform 0.2s ease;
    }
    .topic-card:hover .pixel-sprite-img { transform: scale(1.1) translateY(-4px); }
  </style>""")
    
    # Replace SVG sprite boxes with img
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Ant-Man Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/antman.png" class="pixel-sprite-img" alt="Ant-Man"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Doctor Strange Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/doctorstrange.png" class="pixel-sprite-img" alt="Doctor Strange"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Vision Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/vision.png" class="pixel-sprite-img" alt="Vision"></div></div>',
        content, flags=re.DOTALL
    )
    with open(m1_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated mission-01.html with PNG sprites!")

# 2. Update Mission 02
m2_path = "mission-02.html"
if os.path.exists(m2_path):
    with open(m2_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if ".pixel-sprite-img" not in content:
        content = content.replace("</style>", """
    .pixel-sprite-img {
      max-width: 100px; max-height: 115px; width: auto; height: auto;
      object-fit: contain; image-rendering: pixelated; image-rendering: crisp-edges;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2)); transition: transform 0.2s ease;
    }
    .topic-card:hover .pixel-sprite-img { transform: scale(1.1) translateY(-4px); }
  </style>""")
    
    # Replace sprites
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Stacking Vibranium Shields.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/captainamerica.png" class="pixel-sprite-img" alt="Captain America"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Groot Chibi.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/groot.png" class="pixel-sprite-img" alt="Groot"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Iron Man Armor Vault.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/ironman.png" class="pixel-sprite-img" alt="Iron Man"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Scarlet Witch Reality Spheres.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/scarletwitch.png" class="pixel-sprite-img" alt="Scarlet Witch"></div></div>',
        content, flags=re.DOTALL
    )
    with open(m2_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated mission-02.html with PNG sprites!")

# 3. Update Mission 03
m3_path = "mission-03.html"
if os.path.exists(m3_path):
    with open(m3_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if ".pixel-sprite-img" not in content:
        content = content.replace("</style>", """
    .pixel-sprite-img {
      max-width: 100px; max-height: 115px; width: auto; height: auto;
      object-fit: contain; image-rendering: pixelated; image-rendering: crisp-edges;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2)); transition: transform 0.2s ease;
    }
    .topic-card:hover .pixel-sprite-img { transform: scale(1.1) translateY(-4px); }
  </style>""")
    
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Hawkeye Chibi.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/hawkeye.png" class="pixel-sprite-img" alt="Hawkeye"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Spider-Man Chibi.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/spiderman.png" class="pixel-sprite-img" alt="Spider-Man"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- War Machine Helmet.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/warmachine.png" class="pixel-sprite-img" alt="War Machine"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Quicksilver Silver Hair.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/quicksilver.png" class="pixel-sprite-img" alt="Quicksilver"></div></div>',
        content, flags=re.DOTALL
    )
    with open(m3_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated mission-03.html with PNG sprites!")

# 4. Update Mission 04
m4_path = "mission-04.html"
if os.path.exists(m4_path):
    with open(m4_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if ".pixel-sprite-img" not in content:
        content = content.replace("</style>", """
    .pixel-sprite-img {
      max-width: 100px; max-height: 115px; width: auto; height: auto;
      object-fit: contain; image-rendering: pixelated; image-rendering: crisp-edges;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2)); transition: transform 0.2s ease;
    }
    .topic-card:hover .pixel-sprite-img { transform: scale(1.1) translateY(-4px); }
  </style>""")
    
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Black Panther Helmet.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/blackpanther.png" class="pixel-sprite-img" alt="Black Panther"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Rocket Ears.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/rocket.png" class="pixel-sprite-img" alt="Rocket"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Golden Asgardian Hair.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/thor.png" class="pixel-sprite-img" alt="Thor"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Wolverine Cowl Horns.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/wolverine.png" class="pixel-sprite-img" alt="Wolverine"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Golden Mohawk.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/captainmarvel.png" class="pixel-sprite-img" alt="Captain Marvel"></div></div>',
        content, flags=re.DOTALL
    )
    with open(m4_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated mission-04.html with PNG sprites!")

# 5. Update Mission 05
m5_path = "mission-05.html"
if os.path.exists(m5_path):
    with open(m5_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if ".pixel-sprite-img" not in content:
        content = content.replace("</style>", """
    .pixel-sprite-img {
      max-width: 100px; max-height: 115px; width: auto; height: auto;
      object-fit: contain; image-rendering: pixelated; image-rendering: crisp-edges;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2)); transition: transform 0.2s ease;
    }
    .topic-card:hover .pixel-sprite-img { transform: scale(1.1) translateY(-4px); }
  </style>""")
    
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Loki Golden Horned Helmet.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/loki.png" class="pixel-sprite-img" alt="Loki"></div></div>',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'<div class="char-sprite">\s*<svg viewBox="0 0 24 28".*?<!-- Red / Crimson Hair.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/blackwidow.png" class="pixel-sprite-img" alt="Black Widow"></div></div>',
        content, flags=re.DOTALL
    )
    with open(m5_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated mission-05.html with PNG sprites!")

# 6. Update Missions Directory (missions.html)
ms_path = "missions.html"
if os.path.exists(ms_path):
    with open(ms_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if ".pixel-sprite-img" not in content:
        content = content.replace("</style>", """
    .pixel-sprite-img {
      max-width: 115px; max-height: 130px; width: auto; height: auto;
      object-fit: contain; image-rendering: pixelated; image-rendering: crisp-edges;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2)); transition: transform 0.2s ease;
    }
    .mission-card:hover .pixel-sprite-img { transform: scale(1.1) translateY(-4px); }
  </style>""")
    
    # Cap (M1)
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Captain America Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/captainamerica.png" class="pixel-sprite-img" alt="Captain America"></div></div>',
        content, flags=re.DOTALL
    )
    # Hulk (M2)
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Hulk Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/hulk.png" class="pixel-sprite-img" alt="Hulk"></div></div>',
        content, flags=re.DOTALL
    )
    # Iron Man (M3)
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Iron Man Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/ironman.png" class="pixel-sprite-img" alt="Iron Man"></div></div>',
        content, flags=re.DOTALL
    )
    # Thor (M4)
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Thor Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/thor.png" class="pixel-sprite-img" alt="Thor"></div></div>',
        content, flags=re.DOTALL
    )
    # Black Widow (M5)
    content = re.sub(
        r'<div class="char-sprite">\s*<!-- Pixel Black Widow Chibi Sprite -->.*?</div>\s*</div>',
        '<div class="char-sprite"><img src="assets/blackwidow.png" class="pixel-sprite-img" alt="Black Widow"></div></div>',
        content, flags=re.DOTALL
    )
    with open(ms_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated missions.html with PNG sprites!")

print("All mission directory and hub pages updated with transparent PNG sprites!")
