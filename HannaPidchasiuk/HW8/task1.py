# Implement your own print function. It should work on all operating systems.
import os
import sys


def my_print(*args):
    temp_line = ''
    for item in args:
        temp_line += str(item) + " "
    sys.stdout.write(temp_line)
    sys.stdout.write("\n")


if __name__ == "__main__":
    my_print(1, "sdfg", (3, 4), True, 2.333, [1, 2])
    print(1, "sdfg", (3, 4), True, 2.333, [1, 2])
