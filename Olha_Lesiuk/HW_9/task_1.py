
from functools import reduce


def dec(operator=""):
    def features(fn):
        def add_some_decorations(*args):
            res = reduce(fn, *args)
            print(f"Result of {fn.__name__}: {res}")
            print(f"Operator: {operator}")
            print("Numbers: ", end="")
            print(*args)
            print()
            return res
        return add_some_decorations
    return features


@dec(operator="+")
def add(a, b):
    """Addition of a list of arguments"""
    return a + b


@dec(operator="*")
def sub(a, b):
    """Multiplication of a list of arguments"""
    return a * b


x = add([5, 2])

y = sub([1, 4])
