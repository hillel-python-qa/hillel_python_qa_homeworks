def maximum(x: list, amount_of_result=1):
    """
            Implementing my own max function.
            """

    max_number = x[0]
    second_max_number = x[0]
    if amount_of_result >= 2 or amount_of_result < 1:
        raise Exception("The function should return 2 max values from the list")
    elif amount_of_result == 2:
        for i in x:
            if i > max_number:
                max_number = i
        for i in x:
            if max_number > i > second_max_number:
                second_max_number = i
        return max_number, second_max_number
    else:
        for i in x:
            if i > max_number:
                max_number = i
    return max_number


def minimum(x: list, amount_of_result=1):
    """
            Implementing my own min function.
            """

    min_number = x[0]
    second_min_number = x[0]
    if amount_of_result >= 2 or amount_of_result < 1:
        raise Exception("The function should return 2 max values from the list")
    elif amount_of_result == 2:
        for i in x:
            if i < min_number:
                min_number = i
        for i in x:
            if min_number < i < second_min_number:
                second_min_number = i
        return min_number, second_min_number
    else:
        for i in x:
            if i < min_number:
                min_number = i
    return min_number
