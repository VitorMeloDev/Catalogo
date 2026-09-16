# Python Basics
# Syntax, variables, types, operators and control flow


# ==========================================================
# Variables and Types
# ==========================================================

name: str = "Knight"
age: int = 25
health: float = 100.0
alive: bool = True
nothing: None = None

print(type(name))
print(type(age))
print(type(health))
print(type(alive))
print(type(nothing))


# ==========================================================
# Arithmetic
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
# Comparisons and Logic
# ==========================================================

print(a == b)
print(a != b)
print(a > b)
print(a < b)

has_key = True
door_open = False

print(has_key and door_open)
print(has_key or door_open)
print(not door_open)


# ==========================================================
# Strings
# ==========================================================

message = "Hello Python"

print(message[0])
print(message[-1])
print(message[0:5])
print(len(message))
print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Python", "World"))


# ==========================================================
# Formatting and Conversion
# ==========================================================

level = 10

print(f"{name} is level {level}")

number = int("42")
decimal = float("3.14")
text = str(42)

print(number, decimal, text)


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
# Loops
# ==========================================================

for number in range(5):
    print(number)

count = 0

while count < 3:
    print(count)
    count += 1


# ==========================================================
# break / continue
# ==========================================================

for number in range(10):

    if number == 3:
        continue

    if number == 7:
        break

    print(number)


# ==========================================================
# enumerate / zip
# ==========================================================

items = ["sword", "bow", "shield"]

for index, item in enumerate(items):
    print(index, item)

names = ["Knight", "Mage"]
levels = [10, 20]

for name, level in zip(names, levels):
    print(name, level)


# ==========================================================
# Input
# ==========================================================

# user_name = input("Name: ")
# print(user_name)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Basics reference")
