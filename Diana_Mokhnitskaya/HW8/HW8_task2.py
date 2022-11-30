def my_own_filter(add, sequence):
    result = []
    for item in sequence:
        if add(item):
            result.append(item)
    return result


def add(item):
    if item % 2 == 0:
        return True
    else:
        return False
