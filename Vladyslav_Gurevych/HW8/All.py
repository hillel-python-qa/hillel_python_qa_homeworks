def own_all(arr: list) -> bool:
    """
        This function takes an argument(list) and returns a boolean value if one of the values is False
    """
    for element in arr:
        if not element:
            return False
    return True


if __name__ == "__main__":
    arr = [1, 4, 5, {}]
    arr1 = [1, 4, 5]
    print(own_all(arr))
    print(own_all(arr1))

    print(all(arr))
    print(all(arr1))
