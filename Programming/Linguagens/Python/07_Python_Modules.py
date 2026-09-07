# Python Modules
# Imports, Packages, Standard Library and __main__


# ==========================================================
# Importing a Module
# ==========================================================

import math

print(math.sqrt(25))
print(math.pi)


# ==========================================================
# Import Specific Names
# ==========================================================

from math import sqrt, pi

print(sqrt(16))
print(pi)


# ==========================================================
# Import Alias
# ==========================================================

import datetime as dt

now = dt.datetime.now()

print(now)


# ==========================================================
# Module Alias
# ==========================================================

import math as mathematics

print(mathematics.floor(3.8))


# ==========================================================
# sys Module
# ==========================================================

import sys

print(sys.version)
print(sys.argv)


# ==========================================================
# os Module
# ==========================================================

import os

print(os.getcwd())
print(os.name)


# ==========================================================
# pathlib
# ==========================================================

from pathlib import Path

current = Path.cwd()

print(current)

file = current / "example.txt"

print(file)


# ==========================================================
# Checking Paths
# ==========================================================

path = Path("example.txt")

print(path.exists())
print(path.is_file())
print(path.is_dir())


# ==========================================================
# Creating Directories
# ==========================================================

directory = Path("example_folder")

directory.mkdir(exist_ok=True)


# ==========================================================
# Iterating Directory Contents
# ==========================================================

for item in Path(".").iterdir():
    print(item)


# ==========================================================
# Importing Your Own Module
# ==========================================================

# Suppose we have:
#
# math_utils.py
#
# def add(a: int, b: int) -> int:
#     return a + b
#
# Then:
#
# from math_utils import add
#
# print(add(10, 20))


# ==========================================================
# Package Structure
# ==========================================================

# project/
# ├── main.py
# └── utils/
#     ├── __init__.py
#     └── math_utils.py


# ==========================================================
# __name__
# ==========================================================

print(__name__)


# ==========================================================
# Main Guard
# ==========================================================

def main() -> None:
    print("Program started")


if __name__ == "__main__":
    main()


# ==========================================================
# Useful Standard Library Modules
# ==========================================================

import random
import json
import re
import statistics

print(random.randint(1, 10))

data = {"name": "Vitor", "level": 10}

json_text = json.dumps(data)

print(json_text)

print(statistics.mean([10, 20, 30]))

pattern = r"\d+"

print(re.findall(pattern, "Player 42"))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Modules reference")
