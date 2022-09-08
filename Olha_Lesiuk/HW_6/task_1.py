import os
from random import randint
left_operand = []
right_operand = []
operations = []
list_with_tuples = []

for element in list(range(101)):
    left_operand = randint(1, 100)
    right_operand = randint(1, 100)
    operations = randint(1, 3)
    list_with_tuples.append((left_operand, right_operand, operations))
print(list_with_tuples)

os.makedirs("test/data", exist_ok=True)
with open("test/data/list_with_tuples.txt", "w") as file:
    for element in list_with_tuples:
        file.write(f'{element[0]} {element[1]} {element[2]}\n')
