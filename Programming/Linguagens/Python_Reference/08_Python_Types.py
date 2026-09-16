# Python Types and Type Hints
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
