# you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where the first element
# is the index and the second is the value. [(index, value)]. accordingly, elements with an even
# index are placed in another list of tuples with the same format as in the case with odd indices.

arr = [1, 2, 3, 4, 5, 6, 7, 8]
even_list, odd_list = [], []
for index, element in enumerate(arr):
    if index % 2 == 0:
        even_list.append((index, element))
    else:
        odd_list.append((index, element))

print(even_list)
print(odd_list)
