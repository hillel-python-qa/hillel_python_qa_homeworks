def my_filter(callback, sequence):
    return [item for item in sequence if callback(item)]


test_velue = (1, 2, 3, 0, 5, 7, 0)
print(my_filter(lambda item: True if item else False, test_velue))
print(list(filter(lambda item: True if item else False, test_velue)))
