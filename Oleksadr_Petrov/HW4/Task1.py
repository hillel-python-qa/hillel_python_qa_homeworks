def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


values = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2]
odd = []
even = []

for i in range(0, len(values)):
    if is_even(values[i]):
        even.append((i, values[i]))
    else:
        odd.append((i, values[i]))

print(even)
print(odd)
