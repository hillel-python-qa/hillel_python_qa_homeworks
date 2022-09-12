def own_max(arr: list, amount_of_result: int = 1) -> list:
    """
       This function takes arguments(list and amount_of_result) and returns a list with a max value.
       The number of output values can be changed by entering amount_of_result.
    """
    result = []
    temp = arr[:]
    for _ in range(amount_of_result):
        max_digit = temp[0]
        for i in range(1, len(temp)):
            if max_digit < temp[i]:
                max_digit = temp[i]
            else:
                continue
        result.append(max_digit)
        temp.remove(max_digit)
    return result


def own_min(arr: list, amount_of_result: int = 1) -> list:
    """
        This function takes arguments(list and amount_of_result) and returns a list with a max value.
        The number of output values can be changed by entering amount_of_result.
    """
    result = []
    temp = arr[:]
    for _ in range(amount_of_result):
        min_digit = temp[0]
        for i in range(1, len(temp)):
            if min_digit > temp[i]:
                min_digit = temp[i]
            else:
                continue
        result.append(min_digit)
        temp.remove(min_digit)

    return result


if __name__ == "__main__":
    digit = [172, 292, -1, 52, 5, 5000, 18, -909, 547, 123]

    print(own_max(digit, 2))
    print(own_min(digit, 5))
