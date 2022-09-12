import os

with open('./test/data/tuples_1.txt', 'r') as file:
    tuples = file.read().splitlines()
for digits in tuples:
    line = digits.split(' ')
    left = int(line[0])
    right = int(line[1])
    operation = int(line[2])

    if operation == 1:
        math = left + right
        print (f'{left}+{right}={math}')
    elif operation == 2:
        math = left - right
        print(f'{left}-{right}={math}')
    else:
        math = left * right
        print(f'{left}*{right}={math}')
