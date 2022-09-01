def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


values = [1, 2, 3, 4, 5, 6, 7, 8]
odd = []
even = []

for element in list:
    if isEven(element):
        even.append((list.index(element), element))
    else:
        odd.append((list.index(element), element))

print(even)
print(odd)
