from typing import Callable


def filter_func(callback: Callable, sequence: list) -> list:
    """
    Returns items from sequence based on conditional callback
    """
    return [item for item in sequence if callback(item)]


def condition_numbers(number):
    """
    Conditional function
    """
    if number < 4.5:
        return False
    else:
        return True


def condition_m(word):
    """
    Conditional function
    """
    if word.startswith('M'):
        return True
    else:
        return False


if __name__ == '__main__':
    names = ['David', 'Martin', 'Maine', 'Rebecca', 'Lucy']
    numbers = [1, 2, 3, 4.4, 2, 1, 3, 4.6, 5, 6, 6, 7, ]
    print(filter_func(condition_numbers, numbers))
    print(filter_func(condition_m, names))
