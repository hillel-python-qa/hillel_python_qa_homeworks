from typing import Callable


def name_decorator(function_to_decorate: Callable):
    def inner(a: int, b: int):
        return f'The {function_to_decorate.__name__} is {function_to_decorate(a, b)}'

    return inner


@name_decorator
def sum_of_digit(a: int, b: int) -> int:
    return a + b


@name_decorator
def sum_of_multi(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    print(sum_of_multi(5, 4))
    print(sum_of_digit(1, 4))
