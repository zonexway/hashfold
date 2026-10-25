import time 
check_interval = 7200
chunk_size = 4096

def ask(prompt, default):
    while True:
        str = input(f"{prompt} (default {default}): ").strip()
        if not str:
            return default
        if str.isdigit() and int(str) > 0:
            return int(str)


print('Start configuration')
check_interval = ask("Choose time for checking (seconds)", check_interval)
chunk_size = ask("Choose chunk size", chunk_size)
