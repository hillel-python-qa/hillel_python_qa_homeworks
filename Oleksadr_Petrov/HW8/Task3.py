def custom_map(callback: callable, sequence: iter):
    return [callback(value) for value in sequence]


def even_numbers(number: int):
    if number % 2 == 0:
        return True
    else:
        return False


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
even = custom_map(even_numbers, numbers)
even = list(even)
print(list(even))
