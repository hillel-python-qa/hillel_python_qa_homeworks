import os
from random import randint
a_left_operand = []
b_right_operand = []
c_operations = []
list_with_tuples = []

for element in list(range(101)):
    a_left_operand = randint(1, 100)
    b_right_operand = randint(1, 100)
    c_operations = randint(1, 3)
    list_with_tuples.append((a_left_operand, b_right_operand, c_operations))
print(list_with_tuples)

os.makedirs("test/data")
with open("test/data/list_with_tuples.txt", "w") as file:
    for element in list_with_tuples:
        file.write(f'{element[0]} {element[1]} {element[2]}\n')
