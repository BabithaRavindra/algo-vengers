import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

for m in re.finditer(r'data:image/svg\+xml,[^"\'\)]+', text):
    print("MATCH:", m.group(0)[:150])

for m in re.finditer(r'<svg[^>]*>.*?</svg>', text, re.DOTALL):
    s = m.group(0)
    if "shield" in s.lower() or "hammer" in s.lower() or "reactor" in s.lower() or "mjolnir" in s.lower() or "widow" in s.lower():
        print("FOUND EMBLEM SVG:", s[:200])
