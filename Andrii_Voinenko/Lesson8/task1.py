import sys


def my_print(sequence: list):
    for item in sequence:
        sys.stdout.write(f"{str(item)}\n")


t = [1, 1.2, '', 's']
my_print(t)
