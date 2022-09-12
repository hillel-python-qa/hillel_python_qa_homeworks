# Implement your own implementation of the function map


def my_map(callback: callable, sequence: iter) -> list:
    return [callback(item) for item in sequence]


if __name__ == "__main__":
    test_sequence = ["test", "slfkf", "skjfhd", "sjhlobavlisdnv"]

    print(list(map(len, test_sequence)))
    print(my_map(len, test_sequence))
