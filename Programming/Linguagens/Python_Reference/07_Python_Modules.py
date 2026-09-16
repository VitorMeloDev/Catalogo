# Python Modules and Packages
# Imports, namespaces, paths and program entry points


# ==========================================================
# Importing
# ==========================================================

import math

print(math.sqrt(25))
print(math.pi)


# ==========================================================
# Alias
# ==========================================================

import datetime as dt

print(dt.datetime.now())


# ==========================================================
# Import Specific Names
# ==========================================================

from math import sqrt, pi

print(sqrt(16))
print(pi)


# ==========================================================
# Standard Library
# ==========================================================
# math     = mathematics
# sys      = interpreter/process information
# os       = operating system
# pathlib  = filesystem paths
# json     = JSON
# csv      = CSV
# re       = regular expressions
# datetime = dates and times


# ==========================================================
# pathlib
# ==========================================================

from pathlib import Path

path = Path("example.txt")

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.exists())


# ==========================================================
# Package Structure
# ==========================================================
# project/
# ├── main.py
# └── game/
#     ├── __init__.py
#     ├── player.py
#     └── enemy.py
#
# Example:
# from game.player import Player


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
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Modules reference")
