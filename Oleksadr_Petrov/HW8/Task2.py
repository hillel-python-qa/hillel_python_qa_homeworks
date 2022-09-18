def custom_filter(callback: callable, sequence: iter):
    return [value for value in sequence if value == callback(value)]


def even_numbers(number: int):
    if number % 2 == 0:
        return number


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
even = custom_filter(even_numbers, numbers)
even = list(even)
print(list(even))
