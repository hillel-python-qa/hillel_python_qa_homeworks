numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_index = []
even_index = []

for index, digit in enumerate(numbers):
    if index % 2:
        odd_index.append((index, digit))
    else:
        even_index.append((index, digit))

print(f'Odd index: {odd_index}\nEven index: {even_index}')
