# Python Exceptions
# Exception Handling, Errors and Custom Exceptions


# ==========================================================
# Basic Exception
# ==========================================================

# print(10 / 0)


# ==========================================================
# Try / Except
# ==========================================================

try:
    number = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# ==========================================================
# Catching the Exception
# ==========================================================

try:
    number = int("Python")
except ValueError as error:
    print(error)


# ==========================================================
# Multiple Exceptions
# ==========================================================

try:
    number = int("10")
    result = 100 / number

    print(result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")


# ==========================================================
# Exception Hierarchy
# ==========================================================

# Exception
# ├── ValueError
# ├── TypeError
# ├── OSError
# │   ├── FileNotFoundError
# │   └── PermissionError
# └── ...


# ==========================================================
# General Exception
# ==========================================================

try:
    result = 10 / 0

except Exception as error:
    print(f"Error: {error}")


# ==========================================================
# Raise
# ==========================================================

def set_age(age: int) -> None:

    if age < 0:
        raise ValueError("Age cannot be negative")

    print(f"Age: {age}")


set_age(25)


# ==========================================================
# Validation
# ==========================================================

def set_score(score: float) -> None:

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    print(f"Score: {score}")


try:
    set_score(150)

except ValueError as error:
    print(error)


# ==========================================================
# Custom Exception
# ==========================================================

class InsufficientFundsError(Exception):
    pass


balance = 100
withdraw = 150

try:

    if withdraw > balance:
        raise InsufficientFundsError("Insufficient funds")

    balance -= withdraw

except InsufficientFundsError as error:
    print(error)


# ==========================================================
# Custom Exception with Data
# ==========================================================

class InvalidScoreError(ValueError):

    def __init__(self, score: float) -> None:
        self.score = score

        super().__init__(
            f"Invalid score: {score}"
        )


try:

    score = 150

    if score < 0 or score > 100:
        raise InvalidScoreError(score)

except InvalidScoreError as error:
    print(error)
    print(error.score)


# ==========================================================
# Finally
# ==========================================================

try:
    print("Processing")

except Exception:
    print("Error")

finally:
    print("Finished")


# ==========================================================
# Try / Except / Else / Finally
# ==========================================================

try:
    number = int("42")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful")
    print(number)

finally:
    print("Execution finished")


# ==========================================================
# Re-raise
# ==========================================================

try:

    try:
        number = int("Python")

    except ValueError:
        print("Logging error")
        raise

except ValueError:
    print("Exception propagated")


# ==========================================================
# Exception Propagation
# ==========================================================

def convert_number(value: str) -> int:
    return int(value)


def process(value: str) -> None:
    number = convert_number(value)
    print(number)


try:
    process("Python")

except ValueError:
    print("Invalid value")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Exceptions reference")
