import json

import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_FILE_PATH = get_path(filename="SuperHero.json")


with open(JSON_FILE_PATH, "r") as f:
    heroes = json.loads(f.read())

print(heroes)

members = []

for i in heroes['members']:
    members.append(i)

sorted_members = sorted(members, key=lambda x: x['age'], reverse=True)

for member in sorted_members:
    print(member['name'], member['age'])