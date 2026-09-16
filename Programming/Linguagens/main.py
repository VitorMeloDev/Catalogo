from pathlib import Path
import zipfile

base = Path("Python_Reference")
base.mkdir(exist_ok=True)

files = {
"01_Python_Basics.py": '''# Python Basics
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
''',

"02_Python_Collections.py": '''# Python Collections
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
''',

"03_Python_Functions.py": '''# Python Functions
# Definition, parameters, return values and higher-order functions


# ==========================================================
# Basic Function
# ==========================================================

def greet() -> None:
    print("Hello")


greet()


# ==========================================================
# Parameters and Return
# ==========================================================

def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))


# ==========================================================
# Multiple Return Values
# ==========================================================

def get_player() -> tuple[str, int]:
    return "Knight", 10


name, level = get_player()

print(name, level)


# ==========================================================
# Default Parameters
# ==========================================================

def greet_player(name: str, title: str = "Player") -> str:
    return f"{title} {name}"


print(greet_player("Vitor"))
print(greet_player("Vitor", "Developer"))


# ==========================================================
# *args
# ==========================================================

def total(*numbers: int) -> int:
    return sum(numbers)


print(total(1, 2, 3))


# ==========================================================
# **kwargs
# ==========================================================

def show_stats(**stats: int) -> None:

    for name, value in stats.items():
        print(name, value)


show_stats(health=100, mana=50)


# ==========================================================
# Scope
# ==========================================================

global_value = 10


def scope_example() -> None:
    local_value = 20

    print(global_value)
    print(local_value)


scope_example()


# ==========================================================
# Functions as Values
# ==========================================================

def multiply(a: int, b: int) -> int:
    return a * b


operation = multiply

print(operation(3, 4))


# ==========================================================
# Callable
# ==========================================================

from collections.abc import Callable

Operation = Callable[[int, int], int]


def calculate(
    operation: Operation,
    a: int,
    b: int
) -> int:
    return operation(a, b)


print(calculate(add, 5, 3))
print(calculate(multiply, 5, 3))


# ==========================================================
# Lambda
# ==========================================================

double: Callable[[int], int] = lambda value: value * 2

print(double(10))


# ==========================================================
# map / filter
# ==========================================================

numbers = [1, 2, 3, 4]

squares = list(map(lambda number: number ** 2, numbers))
even = list(filter(lambda number: number % 2 == 0, numbers))

print(squares)
print(even)


# ==========================================================
# Recursion
# ==========================================================

def factorial(number: int) -> int:

    if number <= 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))


# ==========================================================
# Docstrings
# ==========================================================

def square(number: int) -> int:
    """Return the square of a number."""
    return number ** 2


print(square.__doc__)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Functions reference")
''',

"04_Python_OOP.py": '''# Python OOP
# Classes, inheritance, abstraction, polymorphism, composition and Protocol
#
# Main ideas:
# Class       = blueprint for objects
# Inheritance = reuse and specialization
# Overriding  = replace inherited behavior
# ABC         = define a required interface
# Polymorphism = same interface, different behavior
# Protocol    = structural interface ("if it has the methods, it fits")


# ==========================================================
# Class and Object
# ==========================================================

class Player:
    pass


player = Player()

print(type(player))


# ==========================================================
# Constructor and Attributes
# ==========================================================

class Character:

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health


character = Character("Knight", 100)

print(character.name)
print(character.health)


# ==========================================================
# Instance Methods
# ==========================================================

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 1

    def level_up(self) -> None:
        self.level += 1


player = Player("Knight")
player.level_up()

print(player.level)


# ==========================================================
# Encapsulation Convention
# ==========================================================

class Account:

    def __init__(self, balance: float) -> None:
        self._balance = balance

    def deposit(self, amount: float) -> None:

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def get_balance(self) -> float:
        return self._balance


account = Account(100)
account.deposit(50)

print(account.get_balance())


# ==========================================================
# Properties
# ==========================================================

class Person:

    def __init__(self, age: int) -> None:
        self._age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value


person = Person(25)

print(person.age)

person.age = 26

print(person.age)


# ==========================================================
# Class Variables
# ==========================================================

class Enemy:

    total_enemies = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Enemy.total_enemies += 1


Enemy("Goblin")
Enemy("Orc")

print(Enemy.total_enemies)


# ==========================================================
# Class Method
# ==========================================================

class Game:

    game_count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Game.game_count += 1

    @classmethod
    def get_game_count(cls) -> int:
        return cls.game_count


Game("Game A")
Game("Game B")

print(Game.get_game_count())


# ==========================================================
# Static Method
# ==========================================================

class MathUtils:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b


print(MathUtils.add(10, 20))


# ==========================================================
# Inheritance
# ==========================================================

class Animal:

    def speak(self) -> None:
        print("Animal sound")


class Dog(Animal):

    def bark(self) -> None:
        print("Woof")


dog = Dog()

dog.speak()
dog.bark()


# ==========================================================
# super()
# ==========================================================
# super() accesses behavior from the parent class.
# It is commonly used when a child extends a parent's __init__.


class Character:

    def __init__(self, name: str) -> None:
        self.name = name


class Warrior(Character):

    def __init__(self, name: str, weapon: str) -> None:
        super().__init__(name)
        self.weapon = weapon


warrior = Warrior("Knight", "Sword")

print(warrior.name)
print(warrior.weapon)


# ==========================================================
# Method Overriding
# ==========================================================
# A child class provides its own implementation of an
# inherited method.


class Enemy:

    def attack(self) -> None:
        print("Generic attack")


class Goblin(Enemy):

    def attack(self) -> None:
        print("Goblin attack")


Goblin().attack()


# ==========================================================
# Abstract Base Class (ABC)
# ==========================================================
# An ABC defines a contract for subclasses.
# abstractmethod means concrete subclasses must implement it.


import abc


class DataProcessor(abc.ABC):

    @abc.abstractmethod
    def validate(self, data: object) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: object) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return 0, "data"


class NumericProcessor(DataProcessor):

    def validate(self, data: object) -> bool:
        return isinstance(data, (int, float))

    def ingest(self, data: object) -> None:
        print(f"Numeric data: {data}")


processor = NumericProcessor()

print(processor.validate(42))
processor.ingest(42)
print(processor.output())


# DataProcessor() would fail because abstract methods
# have not been implemented.


# ==========================================================
# Polymorphism
# ==========================================================
# Different classes can be used through the same interface.


class Weapon(abc.ABC):

    @abc.abstractmethod
    def attack(self) -> None:
        pass


class Sword(Weapon):

    def attack(self) -> None:
        print("Sword attack")


class Bow(Weapon):

    def attack(self) -> None:
        print("Bow attack")


def perform_attack(weapon: Weapon) -> None:
    weapon.attack()


perform_attack(Sword())
perform_attack(Bow())


# ==========================================================
# Polymorphism in Data Processing
# ==========================================================

class Processor(abc.ABC):

    @abc.abstractmethod
    def validate(self, data: object) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: object) -> None:
        pass


class NumericDataProcessor(Processor):

    def validate(self, data: object) -> bool:
        return isinstance(data, (int, float))

    def ingest(self, data: object) -> None:
        print(f"Numeric: {data}")


class TextDataProcessor(Processor):

    def validate(self, data: object) -> bool:
        return isinstance(data, str)

    def ingest(self, data: object) -> None:
        print(f"Text: {data}")


def process_data(processor: Processor, data: object) -> None:

    if processor.validate(data):
        processor.ingest(data)


process_data(NumericDataProcessor(), 42)
process_data(TextDataProcessor(), "Hello")


# ==========================================================
# Composition
# ==========================================================
# Composition means one object contains another object.


class Engine:

    def start(self) -> None:
        print("Engine started")


class Car:

    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> None:
        self.engine.start()
        print("Car started")


Car().start()


# ==========================================================
# Protocol
# ==========================================================
# Protocol describes what an object must provide.
# A class does not need to inherit from the Protocol.


from typing import Protocol


class ExportPlugin(Protocol):

    def process_output(self, data: list[str]) -> None:
        ...


class CSVPlugin:

    def process_output(self, data: list[str]) -> None:
        print(",".join(data))


class JSONPlugin:

    def process_output(self, data: list[str]) -> None:
        print(data)


def export_data(plugin: ExportPlugin, data: list[str]) -> None:
    plugin.process_output(data)


export_data(CSVPlugin(), ["one", "two", "three"])
export_data(JSONPlugin(), ["one", "two", "three"])


# ==========================================================
# Nested Class
# ==========================================================

class Outer:

    class Inner:

        def hello(self) -> None:
            print("Hello from Inner")


Outer.Inner().hello()


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python OOP reference")
''',

"05_Python_Exceptions.py": '''# Python Exceptions
# Detecting, handling and creating errors


# ==========================================================
# try / except
# ==========================================================

try:
    number = int("42")
    print(number)
except ValueError:
    print("Invalid integer")


# ==========================================================
# Multiple Exceptions
# ==========================================================

try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# ==========================================================
# Exception Object
# ==========================================================

try:
    int("abc")
except ValueError as error:
    print(type(error))
    print(str(error))


# ==========================================================
# raise
# ==========================================================

def validate_age(age: int) -> None:

    if age < 0:
        raise ValueError("Age cannot be negative")


validate_age(25)


# ==========================================================
# Custom Exceptions
# ==========================================================

class InsufficientFundsError(Exception):
    pass


def withdraw(balance: float, amount: float) -> float:

    if amount > balance:
        raise InsufficientFundsError("Insufficient funds")

    return balance - amount


print(withdraw(100, 30))


# ==========================================================
# finally
# ==========================================================

try:
    print("Using resource")
finally:
    print("Cleanup")


# ==========================================================
# try / except / else / finally
# ==========================================================

try:
    number = int("42")
except ValueError:
    print("Invalid input")
else:
    print(f"Valid number: {number}")
finally:
    print("Finished")


# ==========================================================
# Re-raising
# ==========================================================

def parse_number(value: str) -> int:

    try:
        return int(value)
    except ValueError:
        print("Logging error")
        raise


try:
    parse_number("abc")
except ValueError:
    print("Handled by caller")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Exceptions reference")
''',

"06_Python_Files_IO.py": '''# Python Files and I/O
# Files, modes, context managers and standard streams


# ==========================================================
# open()
# ==========================================================
# open() returns a file object.
# It does not return the file contents.


file = open("example.txt", "w")
file.write("Hello Python\\n")
file.close()


# ==========================================================
# Reading
# ==========================================================

file = open("example.txt", "r")

content = file.read()

file.close()

print(content)


# ==========================================================
# File Modes
# ==========================================================
# r = read
# w = write, creates or replaces
# a = append
# x = create only if missing
# + = read and write


# ==========================================================
# readline / readlines
# ==========================================================

with open("example.txt", "r") as file:

    print(file.readline())

with open("example.txt", "r") as file:

    print(file.readlines())


# ==========================================================
# Iterating Over a File
# ==========================================================

with open("example.txt", "r") as file:

    for line in file:
        print(line, end="")


# ==========================================================
# with / Context Manager
# ==========================================================
# with automatically closes the file when the block ends.


with open("example.txt", "r") as file:
    content = file.read()

print(content)


# ==========================================================
# Writing and Appending
# ==========================================================

with open("example.txt", "w") as file:
    file.write("First line\\n")

with open("example.txt", "a") as file:
    file.write("Second line\\n")


# ==========================================================
# tell / seek
# ==========================================================

with open("example.txt", "r") as file:

    print(file.tell())

    print(file.read(3))

    print(file.tell())

    file.seek(0)

    print(file.read(3))


# ==========================================================
# File Errors
# ==========================================================

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except OSError as error:
    print(f"File error: {error}")


# ==========================================================
# Standard Streams
# ==========================================================
# stdin  = input
# stdout = normal output
# stderr = error/diagnostic output


import sys

sys.stdout.write("Normal output\\n")
sys.stderr.write("Error output\\n")


# ==========================================================
# Command-Line Arguments
# ==========================================================

print(sys.argv)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Files and I/O reference")
''',

"07_Python_Modules.py": '''# Python Modules and Packages
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
''',

"08_Python_Types.py": '''# Python Types and Type Hints
# Type annotations, generic collections and static analysis


# ==========================================================
# Basic Annotations
# ==========================================================

name: str = "Knight"
level: int = 10
health: float = 100.0
alive: bool = True


# ==========================================================
# Function Annotations
# ==========================================================

def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))


# ==========================================================
# None
# ==========================================================

def print_message(message: str) -> None:
    print(message)


# ==========================================================
# Generic Collections
# ==========================================================

numbers: list[int] = [1, 2, 3]
names: list[str] = ["Knight", "Mage"]
scores: dict[str, int] = {"Vitor": 100}
point: tuple[int, int] = (10, 20)
ids: set[int] = {1, 2, 3}


# ==========================================================
# Union
# ==========================================================

identifier: int | str

identifier = 42
identifier = "player-42"


# ==========================================================
# None as a Possible Value
# ==========================================================

def find_name(active: bool) -> str | None:

    if active:
        return "Knight"

    return None


name = find_name(False)

if name is not None:
    print(name)


# ==========================================================
# Any
# ==========================================================

from typing import Any

value: Any = 42

value = "text"
value = [1, 2, 3]


# ==========================================================
# Callable
# ==========================================================

from collections.abc import Callable

Operation = Callable[[int, int], int]


def calculate(
    operation: Operation,
    a: int,
    b: int
) -> int:
    return operation(a, b)


print(calculate(add, 5, 3))


# ==========================================================
# TypeVar
# ==========================================================

from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


print(first([1, 2, 3]))
print(first(["a", "b", "c"]))


# ==========================================================
# isinstance and Type Narrowing
# ==========================================================

def describe(value: object) -> str:

    if isinstance(value, int):
        return "integer"

    if isinstance(value, str):
        return "string"

    return "other"


print(describe(42))
print(describe("Python"))


# ==========================================================
# Protocol
# ==========================================================

from typing import Protocol


class Printable(Protocol):

    def print_info(self) -> str:
        ...


class Player:

    def print_info(self) -> str:
        return "Player"


def show_info(value: Printable) -> None:
    print(value.print_info())


show_info(Player())


# ==========================================================
# Dataclass
# ==========================================================

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


print(Point(10, 20))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Types reference")
''',

"09_Python_Advanced.py": '''# Python Advanced
# Iterators, generators, decorators, context managers and enums


# ==========================================================
# Iterator
# ==========================================================

numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==========================================================
# Custom Iterator
# ==========================================================

class Counter:

    def __init__(self, limit: int) -> None:
        self.current = 0
        self.limit = limit

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:

        if self.current >= self.limit:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


for number in Counter(3):
    print(number)


# ==========================================================
# Generator
# ==========================================================

def count_up(limit: int):

    for number in range(limit):
        yield number


for number in count_up(3):
    print(number)


# ==========================================================
# Generator Expression
# ==========================================================

squares = (number ** 2 for number in range(5))

for square in squares:
    print(square)


# ==========================================================
# Decorator
# ==========================================================

from collections.abc import Callable
from functools import wraps
from typing import Any


def log_call(
    function: Callable[..., Any]
) -> Callable[..., Any]:

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        print(f"Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished {function.__name__}")

        return result

    return wrapper


@log_call
def add(a: int, b: int) -> int:
    return a + b


print(add(2, 3))


# ==========================================================
# Context Manager
# ==========================================================

class Resource:

    def __enter__(self) -> "Resource":
        print("Acquire resource")
        return self

    def __exit__(
        self,
        exc_type: object,
        exc_value: object,
        traceback: object
    ) -> None:
        print("Release resource")


with Resource():
    print("Using resource")


# ==========================================================
# Dataclass
# ==========================================================

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    level: int
    health: int


print(Player("Knight", 10, 100))


# ==========================================================
# Enum
# ==========================================================

from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    DEAD = "dead"


print(Status.ACTIVE)
print(Status.ACTIVE.value)


# ==========================================================
# match
# ==========================================================

command = "start"

match command:
    case "start":
        print("Starting")
    case "pause":
        print("Paused")
    case _:
        print("Unknown")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Advanced reference")
''',

"10_Python_Data_Processing.py": '''# Python Data Processing
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

match = re.search(r"\\d+", text)

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
''',

"README.md": '''# Python Reference

This catalog is designed for two situations:

- studying a concept;
- quickly remembering it months later.

Each file groups related concepts. Important terms are explained near
their examples instead of appearing only as isolated syntax.

## Files

01 - Basics
02 - Collections
03 - Functions
04 - OOP
05 - Exceptions
06 - Files and I/O
07 - Modules
08 - Type Hints
09 - Advanced Python
10 - Data Processing

## OOP connection to the current 42 project

The Polymorphic Data Streams project follows this path:

EX0:
ABC -> abstractmethod -> inheritance -> overriding

EX1:
common interface -> polymorphism -> DataStream

EX2:
Protocol -> structural typing -> export plugins

The OOP file contains small examples of all these concepts.

## Quick lookup

Search the folder for terms such as:

super()
ABC
abstractmethod
Protocol
with open
sys.argv
Callable
TypeVar
yield
decorator
json.dumps
'''
}

for name, content in files.items():
    (base / name).write_text(content, encoding="utf-8")

zip_path = Path("/mnt/data/Python_Reference_Simples.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(base.iterdir()):
        z.write(path, arcname=path.name)

print("Created:", zip_path)
print("Files:", len(files))
