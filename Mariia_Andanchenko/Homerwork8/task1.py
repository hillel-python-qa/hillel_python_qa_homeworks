import sys


def my_print(*args):
    new_line = ''
    for arg in args:
        if str(arg).endswith("\n"):
            new_line += str(arg)
        else:
            new_line += str(arg) + " "
    sys.stdout.write(new_line)
    sys.stdout.write("\n")


my_print("Hello\n", 2023, "year")
print("Hello\n", 2023, "year")
