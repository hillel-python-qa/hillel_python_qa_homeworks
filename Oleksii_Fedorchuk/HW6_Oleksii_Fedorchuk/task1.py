import os
import random
import pickle

my_list = []
left_op = 1
right_op = 2
operator = 1
for i in range(100):
    if operator == 3:
        my_list.append((left_op, right_op, operator))
        left_op += random.randint(1, 20)
        right_op += random.randint(1, 20)
        operator = 1

    elif operator == 1:
        my_list.append((left_op, right_op, operator))
        left_op += random.randint(1, 20)
        right_op += random.randint(1, 20)
        operator += 1
    else:
        my_list.append((left_op, right_op, operator))
        left_op += random.randint(1, 20)
        right_op += random.randint(1, 20)
        operator += 1

os.makedirs("task1/data")

with open("task1/data/list.txt", "wb") as file:
    bt_list = pickle.dumps(my_list)
    file.write(bt_list)
