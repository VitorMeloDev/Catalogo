# Python Files & I/O
# Files, Streams, Context Managers and Standard I/O

from typing import IO
import sys


# ==========================================================
# Opening a File
# ==========================================================

# Modes:
# "r" -> read
# "w" -> write / replace
# "a" -> append
# "x" -> create only if it does not exist

file = open("example.txt", "r")

print(type(file))

file.close()


# ==========================================================
# Reading
# ==========================================================

file = open("example.txt", "r")

content = file.read()

print(content)

file.close()


# ==========================================================
# Read N Characters
# ==========================================================

file = open("example.txt", "r")

print(file.read(10))

file.close()


# ==========================================================
# Readline
# ==========================================================

file = open("example.txt", "r")

print(file.readline())
print(file.readline())

file.close()


# ==========================================================
# Readlines
# ==========================================================

file = open("example.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ==========================================================
# Iterating Over a File
# ==========================================================

file = open("example.txt", "r")

for line in file:
    print(line.strip())

file.close()


# ==========================================================
# File Position
# ==========================================================

file = open("example.txt", "r")

print(file.tell())

file.read(5)

print(file.tell())

file.seek(0)

print(file.tell())

file.close()


# ==========================================================
# Writing
# ==========================================================

file = open("output.txt", "w")

file.write("First line\n")
file.write("Second line\n")

file.close()


# ==========================================================
# Writing Multiple Lines
# ==========================================================

lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

file = open("output.txt", "w")

file.writelines(lines)

file.close()


# ==========================================================
# Append
# ==========================================================

file = open("output.txt", "a")

file.write("New line\n")

file.close()


# ==========================================================
# Overwriting
# ==========================================================

# "w" removes the previous content.

file = open("output.txt", "w")

file.write("New content")

file.close()


# ==========================================================
# Exceptions
# ==========================================================

try:
    file = open("does_not_exist.txt", "r")

except FileNotFoundError as error:
    print(error)

except OSError as error:
    print(error)


# ==========================================================
# Type Hint for File Objects
# ==========================================================

def read_file(file: IO[str]) -> str:
    return file.read()


file = open("example.txt", "r")

print(read_file(file))

file.close()


# ==========================================================
# Context Manager
# ==========================================================

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

print(file.closed)


# ==========================================================
# Writing with Context Manager
# ==========================================================

with open("output.txt", "w") as file:
    file.write("Safe write\n")


# ==========================================================
# Transforming a File
# ==========================================================

with open("example.txt", "r") as file:
    lines = file.readlines()

transformed = []

for line in lines:
    transformed.append(line.upper())

with open("output.txt", "w") as file:
    file.writelines(transformed)


# ==========================================================
# Standard Input
# ==========================================================

# input() is essentially a convenient abstraction over stdin.

# name = sys.stdin.readline()
# print(name)


# ==========================================================
# Standard Output
# ==========================================================

sys.stdout.write("Hello from stdout\n")


# ==========================================================
# Standard Error
# ==========================================================

sys.stderr.write("This is an error message\n")


# ==========================================================
# Flush
# ==========================================================

sys.stdout.write("Immediate output\n")
sys.stdout.flush()


# ==========================================================
# Command Line Arguments
# ==========================================================

print(sys.argv)

if len(sys.argv) > 1:
    print(sys.argv[1])


# ==========================================================
# File Processing Pipeline
# ==========================================================

def process_file(input_name: str, output_name: str) -> None:

    with open(input_name, "r") as input_file:
        lines = input_file.readlines()

    processed = []

    for line in lines:
        processed.append(line.rstrip("\n").upper() + "#\n")

    with open(output_name, "w") as output_file:
        output_file.writelines(processed)


# process_file("example.txt", "output.txt")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Files & I/O reference")
