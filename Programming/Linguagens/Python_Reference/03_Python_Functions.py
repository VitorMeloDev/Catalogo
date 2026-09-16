# Python Functions
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
