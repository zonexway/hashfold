import json
import sys
from counter import hash_folder
from pathreader import pathreader
import time 
import signal
from config import check_interval

running = True 

def handlesignal(signum, frame):
    global running
    if not running:
        print("forced exit")
        sys.exit(1)
    running = False
    print("stop after the current cycle")
signal.signal(signal.SIGINT, handlesignal)

pathreader()

while running:
    with open("oldhash.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        for key in data:
            try:
                data[key] = hash_folder(key)
            except Exception as e:
                print(f"Error occurred while hashing {key}: {e}")
    with open("oldhash.json", 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent = 3)
    time.sleep(check_interval)
