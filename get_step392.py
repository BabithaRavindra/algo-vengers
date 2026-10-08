import json

with open(r'C:\Users\Babitha Ravindra\.gemini\antigravity\brain\f1b598a4-a2ab-4446-9d46-24772420f697\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') == 392:
            print(obj.get('content', ''))
            for c in obj.get('tool_calls', []):
                print(c.get('args', {}).get('CodeContent', ''))
