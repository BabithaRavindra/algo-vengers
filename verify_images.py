import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
missing_images = []
all_found_images = set()

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for img in imgs:
        if not img.startswith('http') and not img.startswith('data:'):
            all_found_images.add(img)
            if not os.path.exists(img):
                missing_images.append((f, img))

if missing_images:
    print('Missing images found:', set(missing_images))
else:
    print(f'All {len(all_found_images)} referenced images exist on disk across all {len(html_files)} HTML files!')
