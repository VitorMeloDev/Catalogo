# Python Types
# Type Hints, Generic Collections, Optional Values and Type Checking


# ==========================================================
# Basic Type Hints
# ==========================================================

name: str = "Vitor"
age: int = 25
height: float = 1.71
active: bool = True

print(name, age, height, active)


# ==========================================================
# Function Type Hints
# ==========================================================

def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))


# ==========================================================
# None
# ==========================================================

def print_name(name: str) -> None:
    print(name)


print_name("Vitor")


# ==========================================================
# List Type Hints
# ==========================================================

numbers: list[int] = [1, 2, 3]

names: list[str] = [
    "Alice",
    "Bob",
    "Charlie"
]

print(numbers)
print(names)


# ==========================================================
# Tuple Type Hints
# ==========================================================

position: tuple[float, float] = (10.5, 20.0)

print(position)


# ==========================================================
# Set Type Hints
# ==========================================================

unique_ids: set[int] = {1, 2, 3}

print(unique_ids)


# ==========================================================
# Dictionary Type Hints
# ==========================================================

scores: dict[str, int] = {
    "Vitor": 100,
    "Alice": 90
}

print(scores)


# ==========================================================
# Union
# ==========================================================

def print_id(identifier: int | str) -> None:
    print(identifier)


print_id(10)
print_id("ABC")


# ==========================================================
# Optional Values
# ==========================================================

def find_player(player_id: int) -> str | None:

    if player_id == 1:
        return "Knight"

    return None


player = find_player(2)

print(player)


# ==========================================================
# Type Alias
# ==========================================================

PlayerID = int | str

player_id: PlayerID = "PLAYER_001"

print(player_id)


# ==========================================================
# Any
# ==========================================================

from typing import Any

value: Any = 10

value = "Python"
value = True

print(value)


# ==========================================================
# Callable
# ==========================================================

from collections.abc import Callable

Operation = Callable[[int, int], int]


def multiply(a: int, b: int) -> int:
    return a * b


def execute(
    operation: Operation,
    a: int,
    b: int
) -> int:
    return operation(a, b)


print(execute(multiply, 5, 4))


# ==========================================================
# Generic Functions
# ==========================================================

from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


print(first([1, 2, 3]))
print(first(["A", "B", "C"]))


# ==========================================================
# Type Checking
# ==========================================================

value = 10

print(isinstance(value, int))
print(isinstance(value, str))


# ==========================================================
# Type Narrowing
# ==========================================================

def describe(value: int | str) -> None:

    if isinstance(value, int):
        print(value + 10)

    else:
        print(value.upper())


describe(10)
describe("python")


# ==========================================================
# Dataclass
# ==========================================================

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    level: int


player = Player("Knight", 10)

print(player)
print(player.name)
print(player.level)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Types reference")
