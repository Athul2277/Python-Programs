
import os
import hashlib

folder = "images"
seen = {}
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        with open(path, "rb") as file:
            file_hash = hashlib.sha256(file.read()).hexdigest()
        if file_hash in seen:
            print("Duplicate:", filename, "matches", seen[file_hash])
        else:
            seen[file_hash] = filename
