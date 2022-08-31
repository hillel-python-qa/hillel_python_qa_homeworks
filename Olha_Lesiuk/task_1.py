list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
Oddlist = []
EvenList = []

for i in list_of_elements:
    if i%2 == 0:
        EvenList.append(i)
    else:
        Oddlist.append(i)

EvenList = list(enumerate(EvenList))
Oddlist = list(enumerate(Oddlist))

print("Even numbers", EvenList)
print("Odd numbers", Oddlist)