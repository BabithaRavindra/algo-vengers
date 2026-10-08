import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add CSS for .pixel-sprite img
if ".pixel-sprite img" not in html:
    html = html.replace(".pixel-sprite svg {", """.pixel-sprite img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      image-rendering: pixelated;
      image-rendering: crisp-edges;
    }
    .pixel-sprite svg {""")

# Replace the 7 character sprites
# 1. Iron Man
html = re.sub(
    r'<div class="pixel-sprite ironman-sprite">\s*<!-- Exact Chibi Iron Man.*?</div>\s*</div>',
    '<div class="pixel-sprite ironman-sprite"><img src="assets/ironman.png" alt="Iron Man"></div></div>',
    html, flags=re.DOTALL
)

# 2. Captain America
html = re.sub(
    r'<div class="pixel-sprite captain-sprite">\s*<!-- Exact Chibi Captain America.*?</div>\s*</div>',
    '<div class="pixel-sprite captain-sprite"><img src="assets/captainamerica.png" alt="Captain America"></div></div>',
    html, flags=re.DOTALL
)

# 3. Thor
html = re.sub(
    r'<div class="pixel-sprite thor-sprite">\s*<svg viewBox="0 0 26 32".*?<!-- Silver Winged Helmet.*?</div>\s*</div>',
    '<div class="pixel-sprite thor-sprite"><img src="assets/thor.png" alt="Thor"></div></div>',
    html, flags=re.DOTALL
)

# 4. Hulk
html = re.sub(
    r'<div class="pixel-sprite hulk-sprite">\s*<!-- Exact Chibi Hulk.*?</div>\s*</div>',
    '<div class="pixel-sprite hulk-sprite"><img src="assets/hulk.png" alt="Hulk"></div></div>',
    html, flags=re.DOTALL
)

# 5. Black Widow
html = re.sub(
    r'<div class="pixel-sprite widow-sprite">\s*<!-- Exact Chibi Black Widow.*?</div>\s*</div>',
    '<div class="pixel-sprite widow-sprite"><img src="assets/blackwidow.png" alt="Black Widow"></div></div>',
    html, flags=re.DOTALL
)

# 6. Hawkeye
html = re.sub(
    r'<div class="pixel-sprite hawkeye-sprite">\s*<svg viewBox="0 0 26 32".*?<!-- Hair and Aiming Visor.*?</div>\s*</div>',
    '<div class="pixel-sprite hawkeye-sprite"><img src="assets/hawkeye.png" alt="Hawkeye"></div></div>',
    html, flags=re.DOTALL
)

# 7. Spider-Man
html = re.sub(
    r'<div class="pixel-sprite spiderman-sprite">\s*<!-- Exact Chibi Spider-Man.*?</div>\s*</div>',
    '<div class="pixel-sprite spiderman-sprite"><img src="assets/spiderman.png" alt="Spider-Man"></div></div>',
    html, flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with transparent hero PNG sprites!")
