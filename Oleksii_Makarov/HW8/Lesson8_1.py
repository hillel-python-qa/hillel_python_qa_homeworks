import sys


def my_print(*args):
    """
    Takes argument and print it in the console as a string
    """
    storage = ''
    for item in args:
        storage = storage + str(item)
    sys.stdout.write(storage)


my_print(f"one two three {1, 2, 3}", [1, 2, 3])
