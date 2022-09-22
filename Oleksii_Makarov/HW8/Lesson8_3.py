from typing import Callable


def my_map(callback: Callable, sequence: iter) -> iter:
    """
    Applies a callback function to item from sequence
    """
    return [callback(item) for item in sequence]


def uply_u(inputs: iter) -> iter:
    """
    Applies function for words
    """
    return inputs.upper()


def uply_n(inputs: iter) -> iter:
    """
    Applies function for numbers
    """
    return inputs - inputs / 4


word = ['RollBack']
numb = [2, 3, 4, 5, 6.6]
print(my_map(uply_u, word))
print(my_map(uply_n, numb))
