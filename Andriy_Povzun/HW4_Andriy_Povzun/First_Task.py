all_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []
not_even_numbers = []

for index, number in enumerate(all_numbers):
    if number % 2 == 0:
        even_numbers.append((index, number))
    else:
        not_even_numbers.append((index, number))

