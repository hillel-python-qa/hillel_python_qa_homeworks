# Implement your realization of the function filter
def my_filter(callback: callable, sequence: iter) -> list:
    return [item for item in sequence if callback(item)]


if __name__ == "__main__":
    test_sequence = (1, 2, 3, 0, 5, 7, 0)
    print(my_filter(lambda item: True if item else False, test_sequence))
    print(list(filter(lambda item: True if item else False, test_sequence)))
