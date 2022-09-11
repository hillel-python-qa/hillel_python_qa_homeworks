def own_all(data: list):
    """
        This function takes an argument(list) and returns a boolean value if one of the values is False
    """
    for element in data:
        if not element:
            return False
    return True


if __name__ == "__main__":
    data = [1, 4, 5, {}]
    data1 = [1, 4, 5]
    print(own_all(data))
    print(own_all(data1))

    print(all(data))
    print(all(data1))
