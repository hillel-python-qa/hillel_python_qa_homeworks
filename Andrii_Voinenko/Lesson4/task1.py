elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_elements = []
odd_index = []

even_elements = []
even_index = []

for index, element in enumerate(elements):
    if index % 2 == 0:
        odd_elements.append(element)
        odd_index.append(index)
    else:
        even_elements.append(element)
        even_index.append(index)

odd_elements_tuple = list(zip(odd_index, odd_elements))
even_elements_tuple = list(zip(even_index, even_elements))

print(odd_elements_tuple)
print(even_elements_tuple)
