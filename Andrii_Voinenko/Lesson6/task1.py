import os
import random
import pickle

list_of_tuples = []

for _ in range(0, 100):
    first_value = random.randint(0, 10)
    second_value = random.randint(0, 10)
    third_value = random.randint(1, 3)

    new_tuple = (first_value, second_value, third_value)
    list_of_tuples.append(new_tuple)

os.makedirs('./test/data')
new_file = 'random_values.txt'

with open(os.path.join('test/data', new_file), 'b+a') as file:
    tuples = pickle.dumps(list_of_tuples)
    file.write(tuples)
