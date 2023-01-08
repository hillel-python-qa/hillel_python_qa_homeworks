def my_all(arr):
    temp_arr = [True for item in arr if item]
    if len(temp_arr) < len(arr):
        return False
    else:
        return True


test_value1 = [1, '', 123]
test_value2 = [1, '1232', 0]
test_value3 = [1, '1233', 123]
print(my_all(test_value1))
print(my_all(test_value2))
print(my_all(test_value3))
