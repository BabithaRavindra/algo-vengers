with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
keywords = ['mjolnir', 'hammer', 'shield', 'fist', 'widow', 'hourglass', 'reactor', 'arc']
for kw in keywords:
    matches = [m.start() for m in re.finditer(kw, text, re.IGNORECASE)]
    print(f"Keyword '{kw}': {len(matches)} occurrences")
    for pos in matches[:2]:
        print(text[max(0, pos-100):min(len(text), pos+200)])
        print("="*40)
