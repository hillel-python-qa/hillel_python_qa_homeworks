from typing import Callable


def own_map(callback: Callable, arr: list) -> list:
    """
        This function takes an argument(list) and returns a list modified by a callback function
    """
    return [callback(element) for element in arr]


def own_map_1(callback: Callable, data1: list, data2: list) -> list:
    """
        This function takes arguments(2 lists) and returns a dictionary with the shortest length
    """
    result = {}
    for i in range(callback(data1, data2)):
        result[data1[i]] = data2[i]

    return result


def check_len(data1: list, data2: list) -> int:
    """
        This function takes arguments(2 lists) and returns the shortest length of them
    """
    if len(data1) > len(data2):
        return len(data2)
    else:
        return len(data1)


if __name__ == "__main__":
    example = ["1", "7866"]
    print(own_map(len, example))
    print(own_map(int, example))

    example1 = ["name", "age"]
    example2 = ["viktor", "76", "jk@dd.ua"]
    print(own_map_1(check_len, example1, example2))
