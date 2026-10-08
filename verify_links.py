import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
broken = []
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    links = re.findall(r'href=[\"\']([a-zA-Z0-9_\-]+\.html)[\"\']', content)
    for link in links:
        if not os.path.exists(link):
            broken.append((f, link))

if broken:
    print('Broken links found:', broken)
else:
    print(f'All links verified successfully across {len(html_files)} HTML files! Zero broken routes.')
