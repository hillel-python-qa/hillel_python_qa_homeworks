from typing import Union


def my_max(sequence: list) -> Union[int, str, float]:
    max_number = sequence[0]

    for number in sequence:
        if number > max_number[0:]:
            max_number = number
    return max_number


def my_min(sequence: list) -> Union[int, str, float]:
    min_number = sequence[0]
    for number in sequence[0:]:
        if number < min_number:
            min_number = number
    return min_number


