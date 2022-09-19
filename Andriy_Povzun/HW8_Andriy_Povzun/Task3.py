from typing import Callable, Iterable


def my_map(callback: Callable, sequence: Iterable) -> object:
    result = []
    for item in sequence:
        upgrade_item = callback(item)
        result.append(upgrade_item)
    return result


"""
An alternative to the map() built-in function
"""
if __name__ == '__main__':
    numbers = [12, 15, 20, 35]
    numbers2 = [12, 25, 30, 37]
    print(list(map(lambda number: number * 2, numbers)))
    print(list(my_map(lambda number: number * 2, numbers)))
