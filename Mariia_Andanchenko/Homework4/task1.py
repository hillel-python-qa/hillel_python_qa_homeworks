elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_indexes = []
even_indexes = []

for index, item in enumerate(elements):
    if index % 2 == 0:
        odd_indexes.append((index, item))
    else:
        even_indexes.append((index, item))

print(f'odd_indexes = {odd_indexes}\neven_indexes = {even_indexes}')
