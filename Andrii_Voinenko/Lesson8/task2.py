from typing import Callable, Union

not_filtered = ['Barry', 'Ron', 'Harry', 'Samuel', 'Homer']


def my_filer(function: Callable, sequence: Union[list, tuple]) -> list:
    filtered_list = []
    for item in sequence:
        if function(item):
            filtered_list.append(item)
    return filtered_list


def check(sequence: list) -> bool:
    for element in sequence:
        if element.startswith('H'):
            return True
        else:
            return False


print(my_filer(check, not_filtered))
