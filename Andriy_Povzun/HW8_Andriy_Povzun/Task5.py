from typing import Iterable


def my_all(elements: Iterable) -> bool:
    for element in elements:
        if not element:
            return False
    return True


"""
An alternative to the all() built-in function
"""
if __name__ == '__main__':
    names = ['Andy', 'Sandy', 'Aloha', '', 'Artem', 'Artut', 'Stich']
    numbers = [0, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 1000, 43, 5, 6, 27, 87, 988]
    print(my_all(numbers))
    print(all(numbers))
