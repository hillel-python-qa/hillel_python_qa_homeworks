from typing import Callable

list_of_items = ["BMW", "Bugatti", "Mercedes", "Volkswagen"]


def filter_func(func: Callable, item: list | tuple) -> list:
    filter_list = []
    for items in item:
        if func(items):
            filter_list.append(items)
    return filter_list


def checking(item: list) -> bool:
    for elements in item:
        if elements.startswith("M"):
            return True
        else:
            return False


print(list(filter(lambda item: item.startswith("B"), list_of_items)))
print(filter_func(checking, list_of_items))
