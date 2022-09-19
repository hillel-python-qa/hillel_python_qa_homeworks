import sys


def my_print(*args: object, **kwargs: object) -> object:
    for arg in args:
        sys.stdout.write(str(*args))
    else:
        for kwarg in kwargs:
            sys.stdout.write(str(kwargs))


"""
An alternative to the print() built-in function
"""
