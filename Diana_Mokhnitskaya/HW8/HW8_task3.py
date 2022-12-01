def my_map(my_function, sequence):
    result = []
    for item in sequence:
        yield my_function(item)
    return result


sequence = [5.9, 7, "Hello", "What's up"]


def my_function(item):
    return sequence.append(item)


print(list(my_map(my_function, sequence)))
