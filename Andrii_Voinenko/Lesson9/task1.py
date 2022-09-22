from typing import Callable


def first_decorator(func: Callable):
    def to_print_func(number1, number2):
        return f'{str(func.__name__)}:\n{func(number1, number2)}'

    return to_print_func


@first_decorator
def summation(number1: int, number2: int) -> int:
    return number1 + number2


@first_decorator
def multiplication(number1, number2):
    return number1 * number2


result_sum = summation(2, 2)
result_mult = multiplication(8, 4)
print(result_sum)
print(result_mult)
