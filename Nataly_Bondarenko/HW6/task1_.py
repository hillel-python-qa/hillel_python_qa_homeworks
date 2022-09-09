# #d. You can put data into a text file with the text form or use the pickle module in binary form.
from random import randint

list_of_tuple = list()

for element in range(0, 100, 1):
    left_operand = randint(0, 100)
    right_operand = randint(0, 100)
    operator = randint(1, 3)
    list_of_tuple.append((left_operand, operator, right_operand))

# print(type(list_of_tuple))

import os

try:
    os.makedirs('test/data')
except FileExistsError:
    print("ERROR file exists: 'test/data'")

os.chdir('test/data/')
with open("list_of_tuple.txt", 'w') as file:
    for line in list_of_tuple:
        file.write(f'{line[0]} {line[1]} {line[2]}\n')
