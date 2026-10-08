import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for p in ['enhanced_simulations_part1.py', 'enhanced_simulations_part2.py', 'enhanced_simulations_part3.py', 'enhanced_simulations_part4.py']:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    keys = list(dict.fromkeys(re.findall(r'SIMULATIONS\[["\']([^"\']+)["\']\]', content)))
    print(p, 'keys:', keys)
