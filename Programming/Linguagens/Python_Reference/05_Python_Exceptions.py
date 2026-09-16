# Python Exceptions
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
