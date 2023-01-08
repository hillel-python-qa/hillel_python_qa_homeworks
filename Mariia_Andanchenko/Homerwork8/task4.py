def my_max(arr, counter=1) -> list:
    if counter > len(arr):
        return "Vary long results count!!!"
    result = []
    temp_arr = arr.copy()
    while counter >= 1:
        temp_max = temp_arr[0]
        for index in range(len(temp_arr) - 1):
            if temp_arr[index] > temp_max:
                temp_max = temp_arr[index]
            else:
                continue
        result.append(temp_max)
        temp_arr.remove(temp_max)
        counter -= 1
    return result


def my_min(arr, counter=1) -> list:
    if counter > len(arr):
        return "Vary long results count!!!"
    result = []
    temp_arr = arr.copy()
    while counter >= 1:
        temp_min = temp_arr[0]
        for index in range(len(temp_arr) - 1):
            if temp_arr[index] < temp_min:
                temp_min = temp_arr[index]
            else:
                continue
        result.append(temp_min)
        temp_arr.remove(temp_min)
        counter -= 1
    return result


test_value = [12, 22, 1, 2, 5, 5, 7, 8, 8, 909, 54, 3]

print(my_max(test_value, 10))
print(my_max(test_value, len(test_value)))
print(my_max(test_value, len(test_value)+1))
print(my_min(test_value))
print(my_min(test_value, 5))
print(my_min(test_value, len(test_value)+1))




