from typing import Callable, Union


def my_map(function: Callable, sequence: Union[list, tuple]):
    for item in iter(sequence):
        yield function(item)
