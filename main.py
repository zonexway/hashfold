import json
from counter import hash_folder
from pathreader import pathreader
pathreader()

with open("oldhash.json", 'r', encoding="utf-8") as f:
    data = json.load(f)
    for key in data:
        data[key] = hash_folder(key)
with open("oldhash.json", 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent = 3)