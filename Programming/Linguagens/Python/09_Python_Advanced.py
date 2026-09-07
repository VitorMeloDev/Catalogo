# Python Advanced
# Iterators, Generators, Decorators, Context Managers and Useful Patterns


# ==========================================================
# Iterator
# ==========================================================

numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==========================================================
# Iterator Protocol
# ==========================================================

class Counter:

    def __init__(self, limit: int) -> None:
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self) -> int:

        if self.current >= self.limit:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


counter = Counter(3)

for value in counter:
    print(value)


# ==========================================================
# Generator
# ==========================================================

def count_up_to(limit: int):
    number = 0

    while number < limit:
        yield number
        number += 1


for number in count_up_to(5):
    print(number)


# ==========================================================
# Generator Expression
# ==========================================================

numbers = (number ** 2 for number in range(5))

for number in numbers:
    print(number)


# ==========================================================
# Decorator
# ==========================================================

def log_call(function):

    def wrapper(*args, **kwargs):
        print("Function started")

        result = function(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper


@log_call
def greet(name: str) -> None:
    print(f"Hello, {name}")


greet("Vitor")


# ==========================================================
# functools.wraps
# ==========================================================

from functools import wraps


def log(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Calling function")

        return function(*args, **kwargs)

    return wrapper


@log
def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))
print(add.__name__)


# ==========================================================
# Context Manager
# ==========================================================

class Resource:

    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with Resource():
    print("Using resource")


# ==========================================================
# Context Manager with contextlib
# ==========================================================

from contextlib import contextmanager


@contextmanager
def managed_resource():

    print("Resource acquired")

    try:
        yield

    finally:
        print("Resource released")


with managed_resource():
    print("Working")


# ==========================================================
# Dataclass
# ==========================================================

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float


item = Item("Sword", 100.0)

print(item)


# ==========================================================
# Enum
# ==========================================================

from enum import Enum


class State(Enum):
    MENU = 1
    PLAYING = 2
    PAUSED = 3


state = State.PLAYING

print(state)
print(state.name)
print(state.value)


# ==========================================================
# Pattern Matching
# ==========================================================

def describe_state(state: str) -> None:

    match state:

        case "menu":
            print("Menu")

        case "playing":
            print("Playing")

        case "paused":
            print("Paused")

        case _:
            print("Unknown")


describe_state("playing")


# ==========================================================
# Unpacking
# ==========================================================

player = ("Knight", 10)

name, level = player

print(name)
print(level)


# ==========================================================
# Star Unpacking
# ==========================================================

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Advanced reference")
