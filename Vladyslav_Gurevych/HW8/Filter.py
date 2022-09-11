def own_filter(callback, data: list):
    """
        This function takes arguments(list), makes a callback of another function, and returns a filtered list
    """
    return [element for element in data if callback(element) is True]


def is_it_digit(element):
    """
        This function takes argument, check it for "int" and return a boolean value
    """
    if isinstance(element, int):
        return True
    else:
        return False


def is_it_string(element):
    """
        This function takes an argument, check it for "str" and returns a boolean value
    """
    if isinstance(element, str):
        return True
    else:
        return False


def is_it_float(element):
    """
        This function takes an argument, checks it for a "float" and returns a boolean value
    """
    if isinstance(element, float):
        return True
    else:
        return False


def is_it_true(element):
    """
        This function takes an argument, checks it for "True or False" and returns a boolean value
    """
    if not element:
        return False
    else:
        return True


if __name__ == "__main__":
    example = [3.123, "1", 2, [], (), 5.7, "sksdskxksxn", 5643]

    print(own_filter(is_it_digit, example))
    print(own_filter(is_it_string, example))
    print(own_filter(is_it_float, example))
    print(own_filter(is_it_true, example))
