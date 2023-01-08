def my_map(callback, sequence):
    return [callback(item) for item in sequence]


test_velue = ["test", "1234", "12345", "12345678"]

print(list(map(len, test_velue)))
print(my_map(len, test_velue))
