import json
import os
import hashlib


def from_files(filename):
    try: 
        with open(filename, 'r', encoding = "utf-8-sig") as f:
            return [line.strip().strip('"') for line in f if line.strip()]
    except OSError:
        print(f"Error:Could not read file:", {filename})
        return []

def read_manually():
    paths = []
    while True:
        path = input("Enter a path (or leave empty to finish): ").strip().strip('"')
        if not path:
            break
        paths.append(path)
    return paths

def pathreader():
    paths = []
    while True:
        mode = input("Choose mode (1: from file, 2: manual input, empty for close): ").strip()
        if mode == "1":
            filename = input("Enter the filename containing paths: ").strip('"')
            paths = from_files(filename)
            if paths:
                break
        elif mode == "2":
            paths = read_manually()
            break
        else:
            print("Choosing mode closed.")
            break


    data = {}
    for path in paths:
        if os.path.exists(path):
                data[path] = ''
        else:
            print(f"Warning: Path does not exist:", {path})

    with open('oldhash.json', "w", encoding= "utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


   