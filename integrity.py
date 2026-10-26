
import hashlib
import json
import os

record_file = "checksums.json"

# Load previous checksums
if os.path.exists(record_file):
    with open(record_file, 'r') as f:
        old_data = json.load(f)
else:
    old_data = {}

new_data = {}

folder = input("Enter folder path to monitor: ")

for filename in old_data:
    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        print(filename, "-> Missing File")

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    if os.path.isfile(path) and filename != record_file:
        with open(path, 'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()

        if filename not in old_data:
            print(filename, "-> New File")
        elif old_data[filename] == checksum:
            print(filename, "-> Not Modified")
        else:
            print(filename, "-> Modified")

        new_data[filename] = checksum

# Save current checksums
with open(record_file, 'w') as f:
    json.dump(new_data, f, indent=4)

print("Checksum records updated!")
