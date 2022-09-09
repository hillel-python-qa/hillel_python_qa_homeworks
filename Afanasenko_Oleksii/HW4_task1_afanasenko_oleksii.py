numbers = [1, 2, 3, 4, 5, 6, 7, 8]
list_1 = []
list_2 = []
for index, number in enumerate(numbers):
    if index % 2 == 0:
        list_1.append((index, number))
    else:
        list_2.append((index, number))
print(list_1)
print(list_2)



