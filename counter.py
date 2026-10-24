import json
import hashlib
import config
import os

def hash_folder(folder_path, alg = 'sha256'):
    hash_func = hashlib.new(alg)

    for root, dirs, files  in os.walk(folder_path):
        dirs.sort()
        files.sort()
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_func.update(chunk)
            except (IOError, OSError):
                pass
    return hash_func.hexdigest()







