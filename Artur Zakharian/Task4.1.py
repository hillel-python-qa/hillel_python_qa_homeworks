numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append((numbers.index(number), number))
    else:
        odd.append((numbers.index(number), number))
print(even)
print(odd)
