# Implement your realization of the function filter
def my_filter(callback, sequence) -> list:
    return [item for item in sequence if callback(item)]


def check_is_true(item):
    if item:
        return True
    else:
        return False


if __name__ == "__main__":
    test_sequence = (1, 2, 3, 0, 5, 7, 0)
    print(my_filter(check_is_true, test_sequence))
    print(list(filter(check_is_true, test_sequence)))

