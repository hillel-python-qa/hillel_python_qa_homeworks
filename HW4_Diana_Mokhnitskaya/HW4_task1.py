numbers = [1, 2, 3, 4, 5, 6, 7, 8]
list_with_index_and_value = tuple(enumerate(numbers))

for even in range(0, 7, 2):
    print("Even index:" + str(list_with_index_and_value[even]))
for odd in range(1, 8, 2):
    print("Odd index:" + str(list_with_index_and_value[odd]))
