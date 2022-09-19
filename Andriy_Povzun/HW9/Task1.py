from typing import Union, Callable


def name_func(func: Callable):
    def wrapper(*args):
        return f'{func(*args)}\n{func.__name__}'

    return wrapper


@name_func
def adding_numbers(first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    return first_number + second_number


@name_func
def multiplication_numbers(first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    return first_number * second_number


if __name__ == '__main__':
    print(multiplication_numbers(5, 2))
    print(adding_numbers(10, 15))
