# Implement your own implementation of function max and min
# (* additional argument amount of result, if you pass 2, function should return 2 max values from the list)


def my_max(arr: list, counter=1) -> list:
    result = []
    while counter >= 1:
        temp_max = arr[0]
        for index in range(len(arr) - 1):
            if arr[index] > temp_max:
                temp_max = arr[index]
            else:
                continue
        result.append(temp_max)
        arr.remove(temp_max)
        counter -= 1
    return result


def my_min(arr: list, counter=1) -> list:
    result = []
    while counter >= 1:
        temp_min = arr[0]
        for index in range(len(arr) - 1):
            if arr[index] < temp_min:
                temp_min = arr[index]
            else:
                continue
        result.append(temp_min)
        arr.remove(temp_min)
        counter -= 1
    return result


if __name__ == "__main__":
    list_1 = [12, 22, 1, 2, 5, 5, 7, 8, 8, 909, 54, 3]
    print(my_min(list_1, 3))
    print(my_max(list_1, 4))
