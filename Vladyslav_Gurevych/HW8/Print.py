import sys


def own_print(*args):
    """
        This function takes arguments, convert them to a String and outputs them to console
    """
    info_out = ''
    for arg in args:
        if str(arg).endswith("\n"):
            info_out += str(arg)
        else:
            info_out += str(arg) + ' '
    sys.stdout.write(info_out.rstrip())


if __name__ == "__main__":
    own_print(7, 8, "hjhj\n", True, (3, 3, 2))
