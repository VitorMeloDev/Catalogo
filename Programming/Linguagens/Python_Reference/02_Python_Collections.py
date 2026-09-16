# Python Collections
# Lists, tuples, sets and dictionaries


# ==========================================================
# Lists
# ==========================================================

numbers: list[int] = [10, 20, 30]

numbers.append(40)
numbers.extend([50, 60])
numbers.insert(0, 5)

print(numbers)

numbers.remove(30)
last = numbers.pop()

print(numbers)
print(last)


# ==========================================================
# List Access and Slicing
# ==========================================================

items = ["a", "b", "c", "d", "e"]

print(items[0])
print(items[-1])
print(items[1:4])
print(items[:3])
print(items[2:])
print(items[::-1])


# ==========================================================
# Useful List Operations
# ==========================================================

values = [5, 2, 9, 1]

print(len(values))
print(min(values))
print(max(values))
print(sum(values))
print(2 in values)

values.sort()
print(values)

values.reverse()
print(values)


# ==========================================================
# List Comprehension
# ==========================================================

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
even = [number for number in numbers if number % 2 == 0]

print(squares)
print(even)


# ==========================================================
# Tuples
# ==========================================================

point: tuple[int, int] = (10, 20)

x, y = point

print(x, y)


# ==========================================================
# Sets
# ==========================================================

items: set[str] = {"sword", "bow", "shield"}

items.add("potion")
items.remove("bow")

print(items)


# ==========================================================
# Set Operations
# ==========================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


# ==========================================================
# Dictionaries
# ==========================================================

player: dict[str, object] = {
    "name": "Knight",
    "level": 10,
    "active": True,
}

print(player["name"])
print(player.get("level"))
print(player.get("missing"))

player["health"] = 100
player["level"] = 11

print(player)


# ==========================================================
# Dictionary Iteration
# ==========================================================

for key in player:
    print(key)

for value in player.values():
    print(value)

for key, value in player.items():
    print(key, value)


# ==========================================================
# Dictionary Comprehension
# ==========================================================

numbers = [1, 2, 3, 4]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ==========================================================
# Nested Collections
# ==========================================================

players = [
    {"name": "Knight", "level": 10},
    {"name": "Mage", "level": 20},
]

for player in players:
    print(player["name"], player["level"])


# ==========================================================
# Unpacking
# ==========================================================

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)


# ==========================================================
# Command-Line Arguments
# ==========================================================

import sys

print(sys.argv)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Collections reference")
