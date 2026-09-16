# Python Files and I/O
# Files, modes, context managers and standard streams


# ==========================================================
# open()
# ==========================================================
# open() returns a file object.
# It does not return the file contents.


file = open("example.txt", "w")
file.write("Hello Python\n")
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
    file.write("First line\n")

with open("example.txt", "a") as file:
    file.write("Second line\n")


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

sys.stdout.write("Normal output\n")
sys.stderr.write("Error output\n")


# ==========================================================
# Command-Line Arguments
# ==========================================================

print(sys.argv)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python Files and I/O reference")
