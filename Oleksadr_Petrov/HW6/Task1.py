import random
import os


def write_list_to_file(path: str, file_name: str, list_to_write: list):
    with open(os.path.join(path, file_name), 'w') as file:
        for element in list_to_write:
            file.write(str(element[0]) + " " + str(element[1]) + " " + str(element[2]) + "\n")


values = []
path = "test/data"
file_name = "test_data.txt"
for value in range(100):
    first_value = random.randint(-1000, 1000)
    second_value = random.randint(-1000, 1000)
    action = random.randint(1, 3)
    values.append((first_value, second_value, action))
try:
    os.makedirs(path)
    write_list_to_file(path, file_name, values)
except:
    write_list_to_file(path, file_name, values)
