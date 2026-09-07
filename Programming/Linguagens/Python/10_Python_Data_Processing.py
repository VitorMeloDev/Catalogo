# Python Data Processing
# JSON, CSV, Strings, Regular Expressions and Transformations


# ==========================================================
# JSON
# ==========================================================

import json

player = {
    "name": "Knight",
    "level": 10,
    "active": True
}

json_text = json.dumps(player)

print(json_text)


# ==========================================================
# JSON Formatting
# ==========================================================

formatted = json.dumps(
    player,
    indent=4
)

print(formatted)


# ==========================================================
# JSON Back to Python
# ==========================================================

data = json.loads(json_text)

print(data)
print(data["name"])


# ==========================================================
# JSON File
# ==========================================================

with open("player.json", "w") as file:
    json.dump(player, file, indent=4)


with open("player.json", "r") as file:
    loaded_player = json.load(file)

print(loaded_player)


# ==========================================================
# CSV
# ==========================================================

import csv

players = [
    ["Name", "Level"],
    ["Knight", 10],
    ["Mage", 15]
]

with open("players.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(players)


# ==========================================================
# Reading CSV
# ==========================================================

with open("players.csv", "r", newline="") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# ==========================================================
# String Split
# ==========================================================

text = "Python,C#,C++,C"

languages = text.split(",")

print(languages)


# ==========================================================
# Join
# ==========================================================

languages = ["Python", "C#", "C++"]

text = ", ".join(languages)

print(text)


# ==========================================================
# Strip
# ==========================================================

text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ==========================================================
# Replace
# ==========================================================

text = "I like Java"

print(text.replace("Java", "Python"))


# ==========================================================
# Regular Expressions
# ==========================================================

import re

text = "Player 42 reached level 100"

numbers = re.findall(r"\d+", text)

print(numbers)


# ==========================================================
# Search
# ==========================================================

match = re.search(r"level \d+", text)

if match:
    print(match.group())


# ==========================================================
# Match
# ==========================================================

email = "developer@example.com"

if re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
    print("Valid format")


# ==========================================================
# Transform Collection Data
# ==========================================================

numbers = [1, 2, 3, 4, 5]

squares = [
    number ** 2
    for number in numbers
]

print(squares)


# ==========================================================
# Sorting with Key
# ==========================================================

players = [
    {"name": "Knight", "level": 10},
    {"name": "Mage", "level": 20},
    {"name": "Archer", "level": 15}
]

players.sort(key=lambda player: player["level"])

print(players)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Data Processing reference")
