def my_own_filter(func, *iterable):

    """
    Implementing my own filter function.
    """

    data = []
    if func is None:
        for i in iterable:
            if i:
                data.append(i)
    else:
        for i in iterable:
            if isinstance(i, int) and is_even(i):
                data.append(i)
            elif isinstance(i, list) or isinstance(i, tuple):
                for x in i:
                    if is_even(x):
                        data.append(x)
    return data


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
