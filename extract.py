#!/usr/bin/env python3
"""extract.py <agent output jsonl> <out.json>: pull the last JSON object containing "hoods" from an agent transcript."""
import json, sys
last = None
for line in open(sys.argv[1]):
    try: o = json.loads(line)
    except Exception: continue
    c = (o.get('message') or {}).get('content')
    if not isinstance(c, list): continue
    for x in c:
        if not isinstance(x, dict): continue
        if x.get('type') == 'text' and '"hoods"' in x.get('text', ''): last = x['text']
        if x.get('type') == 'tool_use':
            for v in (x.get('input') or {}).values():
                if isinstance(v, str) and '"hoods"' in v: last = v
t = last[last.index('{'):]
obj, _ = json.JSONDecoder().raw_decode(t)
json.dump(obj, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
print(len(obj.get('hoods', [])), 'hoods', len(obj.get('places', [])), 'places', len(obj.get('walks', [])), 'walks', 'home' in obj)
