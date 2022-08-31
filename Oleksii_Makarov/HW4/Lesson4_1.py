numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_index = []
even_index = []
for index in range(len(numbers)):
    if index % 2:
        odd_index.append((index, numbers[index]))
    else:
        even_index.append((index, numbers[index]))
print(f'Odd index: {odd_index}\nEven index: {even_index}')
