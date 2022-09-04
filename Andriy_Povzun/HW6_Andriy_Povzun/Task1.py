import os

my_list = []
left_operand = 1
right_operand = 2
operator = 1
for i in range(100):
    if operator == 3:
        my_list.append((left_operand, right_operand, operator))
        left_operand += left_operand
        right_operand += right_operand
        operator = 1

    elif operator == 1:
        my_list.append((left_operand, right_operand, operator))
        left_operand += left_operand
        right_operand += right_operand
        operator += 1
    else:
        my_list.append((left_operand, right_operand, operator))
        left_operand += left_operand
        right_operand += right_operand
        operator += 1

os.makedirs('test/data')

with open('test/data/list.txt', 'w') as result:
    for i in range(len(my_list)):
        result.write(f'{my_list[i][0]} {my_list[i][1]} {my_list[i][2]}\n')
