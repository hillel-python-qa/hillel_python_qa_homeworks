import sys

"""
Implementing my own print function that should work on all operating systems.
It directly displays anything written to it to the Console. 
"""


def print_to_stdout(*args, **kwargs):
    for arg in args:
        sys.stdout.write(str(*args))
    else:
        for key, value in kwargs.items():
            sys.stdout.write(str(kwargs))
