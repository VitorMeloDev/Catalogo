# Python Basics
# Variables, Types, Input, Output, Conditions, Loops and Conversions


# ==========================================================
# Variables
# ==========================================================

name = "Vitor"
age = 25
height = 1.71
developer = True

print(name)
print(age)
print(height)
print(developer)


# ==========================================================
# Basic Types
# ==========================================================

integer_number = 10
decimal_number = 3.14
text = "Python"
boolean_value = True

print(type(integer_number))
print(type(decimal_number))
print(type(text))
print(type(boolean_value))


# ==========================================================
# Multiple Assignment
# ==========================================================

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)


# ==========================================================
# Constants
# ==========================================================

# Python does not enforce constants.
# Uppercase names are a convention.

PI = 3.14159
MAX_PLAYERS = 4

print(PI)
print(MAX_PLAYERS)


# ==========================================================
# Arithmetic Operators
# ==========================================================

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# ==========================================================
# Comparison Operators
# ==========================================================

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ==========================================================
# Logical Operators
# ==========================================================

is_adult = age >= 18
has_permission = True

print(is_adult and has_permission)
print(is_adult or has_permission)
print(not is_adult)


# ==========================================================
# Strings
# ==========================================================

language = "Python"

print(language[0])
print(language[-1])
print(len(language))

print(language.upper())
print(language.lower())
print(language.strip())
print(language.replace("Python", "C#"))

print("Py" in language)
print("Java" not in language)


# ==========================================================
# String Formatting
# ==========================================================

player = "Knight"
score = 1500

print("Player:", player)
print("Score:", score)

print(f"{player} scored {score} points")


# ==========================================================
# Input
# ==========================================================

# input() always returns a string.

# user_name = input("Name: ")
# print(user_name)


# ==========================================================
# Type Conversion
# ==========================================================

text_number = "42"

number = int(text_number)
decimal = float("3.14")
text = str(100)
boolean = bool(1)

print(number)
print(decimal)
print(text)
print(boolean)


# ==========================================================
# Conditions
# ==========================================================

score = 75

if score >= 90:
    print("Excellent")

elif score >= 60:
    print("Approved")

else:
    print("Failed")


# ==========================================================
# Ternary Expression
# ==========================================================

status = "Adult" if age >= 18 else "Minor"

print(status)


# ==========================================================
# For Loop
# ==========================================================

for number in range(5):
    print(number)


for number in range(1, 6):
    print(number)


# ==========================================================
# While Loop
# ==========================================================

counter = 0

while counter < 5:
    print(counter)
    counter += 1


# ==========================================================
# Break
# ==========================================================

for number in range(10):

    if number == 5:
        break

    print(number)


# ==========================================================
# Continue
# ==========================================================

for number in range(5):

    if number == 2:
        continue

    print(number)


# ==========================================================
# Enumerate
# ==========================================================

languages = ["C", "C#", "Python"]

for index, language in enumerate(languages):
    print(index, language)


# ==========================================================
# Zip
# ==========================================================

names = ["Alice", "Bob", "Charlie"]
scores = [100, 80, 95]

for name, score in zip(names, scores):
    print(name, score)


# ==========================================================
# Functions
# ==========================================================

def greet(name: str) -> None:
    print(f"Hello, {name}")


greet("Vitor")


# ==========================================================
# Return
# ==========================================================

def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)

print(result)


# ==========================================================
# Default Arguments
# ==========================================================

def create_player(name: str, level: int = 1) -> str:
    return f"{name} - Level {level}"


print(create_player("Knight"))
print(create_player("Mage", 10))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Basics reference")
