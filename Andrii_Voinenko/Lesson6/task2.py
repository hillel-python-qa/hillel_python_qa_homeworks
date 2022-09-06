import pickle

with open('./test/data/random_values.txt', 'b+r') as file:
    byte_list_of_tuples = file.read()
    list_values = pickle.loads(byte_list_of_tuples)
    for element in list_values:
        if element[2] == 1:
            print(f'Result of addition is: {element[0] + element[1]}')
        elif element[2] == 2:
            print(f'Result of subtraction is: {element[0] - element[1]}')
        elif element[2] == 3:
            print(f'Result of multiplication is: {element[0] * element[1]}')
