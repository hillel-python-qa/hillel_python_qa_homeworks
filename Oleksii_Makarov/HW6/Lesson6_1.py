from random import randint
import os

rand_tuples = list()
for temp in range(0, 100):
    right = randint(0, 100)
    left = randint(0, 100)
    operation = randint(1, 3)
    rand_tuples.append((right, left, operation))
os.makedirs('./test/data', exist_ok=True)
with open('./test/data/tuples_1.txt', 'w') as file:
    for line in rand_tuples:
        file.write(f'{line[0]} {line[1]} {line[2]}\n')
