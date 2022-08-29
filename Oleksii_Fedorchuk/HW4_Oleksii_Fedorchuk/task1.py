list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []
even_numbers = []
for index, number in enumerate(list_of_elements):
    if index % 2 == 0:
        odd_numbers.append((index, number))
    else:
        even_numbers.append((index, number))
print(f"Odd numbers are: {odd_numbers}")
print(f"Even numbers are: {even_numbers}")

