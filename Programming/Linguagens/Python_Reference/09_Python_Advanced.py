# Python Advanced
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
