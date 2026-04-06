import os

files = os.listdir()

for i, file in enumerate(files):
    if os.path.isfile(file):
        new_name = "file_" + str(i) + ".txt"
        os.rename(file, new_name)
        print("Renamed:", file, "→", new_name)

print("Renaming complete ✅")
