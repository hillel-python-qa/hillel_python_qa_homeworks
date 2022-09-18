umbers = [1, 2, 3, 4, 5, 6, 7, 8]
list_with_index_and_value = tuple(enumerate(numbers))
for number in range(0, len(numbers)):
    if number % 2 == 0:
        print("Even index:" + str(list_with_index_and_value[number]))
    else:
        print("Odd index:" + str(list_with_index_and_value[number]))
