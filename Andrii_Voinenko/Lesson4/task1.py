elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_elements = []
even_elements = []

for index, element in enumerate(elements):
    if index % 2 == 0:
        odd_elements.append((index, element))
    else:
        even_elements.append((index, element))


print(odd_elements)
print(even_elements)
