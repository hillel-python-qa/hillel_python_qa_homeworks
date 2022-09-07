import os
import random
import pickle

my_list = []
left_operand = 1
right_operand = 2
operator = 1
for i in range(100):
    if operator == 3:
        my_list.append((left_operand, right_operand, operator))
        left_operand += random.randint(1, 20)
        right_operand += random.randint(1, 20)
        operator = 1

    elif operator == 1:
        my_list.append((left_operand, right_operand, operator))
        left_operand += random.randint(1, 20)
        right_operand += random.randint(1, 20)
        operator += 1
    else:
        my_list.append((left_operand, right_operand, operator))
        left_operand += random.randint(1, 20)
        right_operand += random.randint(1, 20)
        operator += 1

os.makedirs('test/data')

with open('test/data/list.txt', 'wb') as file:
    byte_list = pickle.dumps(my_list)
    file.write(byte_list)

