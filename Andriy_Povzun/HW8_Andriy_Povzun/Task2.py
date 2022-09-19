from typing import Callable, Iterable


def my_filter(callback: Callable, sequence: Iterable) -> list:
    if callback is None:
        new_sequence = []
        for element in sequence:
            if element:
                new_sequence.append(element)
        return new_sequence
    else:
        result = []
        for item in sequence:
            if callback(item):
                result.append(item)
        return result


"""
An alternative to the filter() built-in function
"""

if __name__ == '__main__':
    names = ['Andy', 'Sandy', 'Aloha', '', 'Artem', 'Artut', 'Stich']
    numbers = [0, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 1000, 43, 5, 6, 27, 87, 988]
    print(list(my_filter(lambda number: number > 900, numbers)))
    print(list(filter(lambda number: number > 900, numbers)))
