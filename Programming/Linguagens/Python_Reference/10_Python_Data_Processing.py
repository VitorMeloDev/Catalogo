# Python Data Processing
# Strings, JSON, CSV, regex and transformation


# ==========================================================
# Strings
# ==========================================================

text = "  Python is powerful  "

print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("powerful", "useful"))


# ==========================================================
# split / join
# ==========================================================

text = "Python,C#,Java"

languages = text.split(",")

print(languages)

print(", ".join(languages))


# ==========================================================
# JSON
# ==========================================================

import json

player = {
    "name": "Knight",
    "level": 10,
    "active": True,
}

json_text = json.dumps(player)

print(json_text)

data = json.loads(json_text)

print(data["name"])


# ==========================================================
# JSON Files
# ==========================================================

with open("player.json", "w") as file:
    json.dump(player, file, indent=4)

with open("player.json", "r") as file:
    loaded = json.load(file)

print(loaded)


# ==========================================================
# CSV
# ==========================================================

import csv

rows = [
    ["name", "level"],
    ["Knight", "10"],
    ["Mage", "20"],
]

with open("players.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("players.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ==========================================================
# Regular Expressions
# ==========================================================

import re

text = "Player ID: 12345"

match = re.search(r"\d+", text)

if match:
    print(match.group())


# ==========================================================
# Transformation
# ==========================================================

raw_values = ["10", "20", "30"]

numbers = [int(value) for value in raw_values]
doubled = [number * 2 for number in numbers]

print(doubled)


# ==========================================================
# Sorting with key
# ==========================================================

players = [
    {"name": "Knight", "level": 20},
    {"name": "Mage", "level": 10},
]

players.sort(key=lambda player: player["level"])

print(players)


# ==========================================================
# Processing Pipeline
# ==========================================================

raw_data = ["10", "20", "30"]

cleaned = [value.strip() for value in raw_data]
converted = [int(value) for value in cleaned]
result = [value * 2 for value in converted]

print(result)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Data Processing reference")
