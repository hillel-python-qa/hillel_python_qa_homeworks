def maximum(array: list, amount_of_result=1):
    """
            Implement your own implementation of function max and min
            (* additional argument amount of result, if you pass 2, function should return 2 max values from the list)
            """

    result = []
    while amount_of_result >= 1:
        maximum_numbers = array[0]
        for index in range(len(array) - 1):
            if array[index] > maximum_numbers:
                maximum_numbers = array[index]
            else:
                continue
        result.append(maximum_numbers)
        array.remove(maximum_numbers)
        amount_of_result -= 1
    return result


def minimum(array: list, amount_of_result=1):
    """
            Implement your own implementation of function max and min
            (* additional argument amount of result, if you pass 2, function should return 2 max values from the list)
            """

    result = []
    while amount_of_result >= 1:
        minimum_numbers = array[0]
        for index in range(len(array) - 1):
            if array[index] > minimum_numbers:
                minimum_numbers = array[index]
            else:
                continue
        result.append(minimum_numbers)
        array.remove(minimum_numbers)
        amount_of_result -= 1
    return result
