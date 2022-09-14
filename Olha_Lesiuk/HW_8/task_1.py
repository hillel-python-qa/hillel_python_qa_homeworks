import sys

"""
Implementing my own print function that should work on all operating systems.
It directly displays anything written to it to the Console. 
"""


def print_to_stdout(*args, **kwargs):
    for arg in args:
        print(*args, file=sys.stdout)
    else:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))
