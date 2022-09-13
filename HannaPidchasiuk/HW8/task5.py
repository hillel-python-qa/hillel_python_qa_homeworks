# Implement your own all function

def my_all(arr: list) -> bool:
    """
        Takes list with any data types inside and returns True in case all elements are True.
    """
    arr_1 = [True for item in arr if item]
    if len(arr_1) < len(arr):
        return False
    else:
        return True


if __name__ == "__main__":
    test_arr = [0, 2, 4, 5, "fd", "fdgfs"]
    print(my_all(test_arr))
