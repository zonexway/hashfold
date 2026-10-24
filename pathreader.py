import json
import hashlib

def pathreader():
    data = {}
    while True:
        key = input("Choose path for check hash (file or directory, empty for close) ")
        if not key:
            break
        data[key] = ""
        with open('oldhash.json', "w", encoding= "utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)




   