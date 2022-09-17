import sys


def printing_func(*args):
    for arg in args:
        sys.stdout.write(str(arg) + "")


printing_func("234")
