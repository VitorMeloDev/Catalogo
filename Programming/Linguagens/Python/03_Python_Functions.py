# Python Functions
# Parameters, Return Values, Scope, Arguments and Higher-Order Functions


# ==========================================================
# Basic Function
# ==========================================================

def greet() -> None:
    print("Hello")


greet()


# ==========================================================
# Parameters
# ==========================================================

def greet_person(name: str) -> None:
    print(f"Hello, {name}")


greet_person("Vitor")


# ==========================================================
# Return
# ==========================================================

def multiply(a: int, b: int) -> int:
    return a * b


result = multiply(5, 4)

print(result)


# ==========================================================
# Multiple Return Values
# ==========================================================

def get_player() -> tuple[str, int]:
    return "Knight", 10


name, level = get_player()

print(name)
print(level)


# ==========================================================
# Default Parameters
# ==========================================================

def create_player(name: str, level: int = 1) -> str:
    return f"{name} - Level {level}"


print(create_player("Knight"))
print(create_player("Mage", 10))


# ==========================================================
# Keyword Arguments
# ==========================================================

def describe_player(name: str, level: int, active: bool) -> None:
    print(name, level, active)


describe_player(
    name="Knight",
    level=10,
    active=True
)


# ==========================================================
# Positional Arguments
# ==========================================================

describe_player("Mage", 20, False)


# ==========================================================
# *args
# ==========================================================

# Permite receber uma quantidade variável de argumentos posicionais.

def sum_numbers(*numbers: int) -> int:
    total = 0

    for number in numbers:
        total += number

    return total


print(sum_numbers(1, 2))
print(sum_numbers(1, 2, 3, 4, 5))


# ==========================================================
# **kwargs
# ==========================================================

# Permite receber argumentos nomeados em quantidade variável.

def print_data(**data: str) -> None:

    for key, value in data.items():
        print(f"{key}: {value}")


print_data(
    name="Vitor",
    language="Python",
    role="Developer"
)


# ==========================================================
# Combining Arguments
# ==========================================================

def configure(
    name: str,
    *tags: str,
    active: bool = True,
    **settings: str
) -> None:

    print(name)
    print(tags)
    print(active)
    print(settings)


configure(
    "Game",
    "Unity",
    "C#",
    active=True,
    version="1.0"
)


# ==========================================================
# Scope
# ==========================================================

global_value = 100


def scope_example() -> None:
    local_value = 50

    print(global_value)
    print(local_value)


scope_example()


# ==========================================================
# Local Variables
# ==========================================================

def counter() -> int:
    value = 0
    value += 1

    return value


print(counter())
print(counter())


# ==========================================================
# Lambda
# ==========================================================

double = lambda number: number * 2

print(double(5))


# ==========================================================
# Functions as Values
# ==========================================================

def add(a: int, b: int) -> int:
    return a + b


operation = add

print(operation(10, 20))


# ==========================================================
# Function as Parameter
# ==========================================================

def apply_operation(
    operation: callable,
    a: int,
    b: int
) -> int:
    return operation(a, b)


print(apply_operation(add, 10, 20))


# ==========================================================
# Built-in Higher-Order Functions
# ==========================================================

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))

print(doubled)
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
# Docstring
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
