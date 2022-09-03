import os

first_operand = []
second_operand = []
operation = []
line = []

for i in range(1, 201, 2):

    if i < 10:
        first_operand.append(i)
    elif 10 <= i < 40:
        s = int(i / 5)
        first_operand.append(s)
    else:
        d = int(i / 4)
        first_operand.append(d)

for i in range(100):
    if i < 10:
        second_operand.append(i)
    elif 10 <= i < 40:
        i = int(i / 4)
        second_operand.append(i)
    else:
        i = int(i / 8)
        second_operand.append(i)

for i in range(100):
    if i % 2 == 0:
        operation.append(1)
    elif i % 3 == 0:
        operation.append(2)
    else:
        operation.append(3)

for i in range(len(first_operand)):
    cell = tuple((first_operand[i], second_operand[i], operation[i]))
    line.append(cell)

os.makedirs('test/data')

with open("test/data/result.txt", 'w') as file:
    for item in line:
        file.write(f'{item[0]} {item[1]} {item[2]}\n')
