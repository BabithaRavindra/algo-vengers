import json

with open(r'C:\Users\Babitha Ravindra\.gemini\antigravity\brain\f1b598a4-a2ab-4446-9d46-24772420f697\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        content = str(obj)
        if 'cursorTemplates' in content and 'svg' in content.lower():
            print("FOUND STEP:", obj.get('step_index'))
            # find cursorTemplates in content
            pos = content.find('cursorTemplates')
            print(content[pos:pos+800])
            print("="*50)
