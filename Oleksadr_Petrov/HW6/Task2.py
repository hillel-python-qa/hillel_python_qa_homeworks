import os
import re

path = "test/data"
file_name = "test_data.txt"
file_content = []

with open(os.path.join(path, file_name), 'r') as file:
    file_content = file.read().splitlines()

for row in file_content:
    operands = re.split(" ", row)
    if int(operands[2]) == 1:
        print(f"%d %c (%d) = %d" % (int(operands[0]), "+", int(operands[1]), int(operands[0]) + int(operands[1])))
    elif int(operands[2]) == 2:
        print(f"%d %c (%d) = %d" % (int(operands[0]), "-", int(operands[1]), int(operands[0]) - int(operands[1])))
    elif int(operands[2]) == 3:
        print(f"%d %c (%d) = %d" % (int(operands[0]), "*", int(operands[1]), int(operands[0]) * int(operands[1])))


