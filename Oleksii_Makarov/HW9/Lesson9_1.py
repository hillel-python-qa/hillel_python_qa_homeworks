from typing import Callable


def name_return_deco(func: Callable):
    def wrapper(*args):
        return f'Function: {func.__name__}. Result: {func(*args)}'

    return wrapper

@name_return_deco
def overly_elaborate_example(num_1: float, num_2: float) -> float:
    '''
    A function that multiplies two numbers one of which num_1 divided by 3.5 and another num_2 is added by 7
    '''
    return (num_1 / 3.5) * (num_2 + 7)


@name_return_deco
def not_so_elaborate_example(words: iter) -> iter:
    '''
    A function that sorts list
    '''
    return sorted(words)


to_sort = 'Welcome to the city.'
print(overly_elaborate_example(7, 12))
print(not_so_elaborate_example(to_sort))
