import sys


def my_print(*args):
    for element in args:
        sys.stdout.write(str(element))
        if args.index(element) == len(args)-1:
            continue
        sys.stdout.write(" ")
    sys.stdout.write("\n")


my_print("Hello")
my_print("World")
my_print(True)
my_print(23131321)
my_print(23131321, "test")
print(2123131, "test")



