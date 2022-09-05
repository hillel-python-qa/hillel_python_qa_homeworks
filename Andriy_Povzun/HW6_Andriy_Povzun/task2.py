import pickle

with open('test/data/list.txt', 'r+b') as file:
    byte_list = file.read()
    my_list = pickle.loads(byte_list)
print(my_list)
results = []
for i in range(len(my_list)):
    if my_list[i][2] == 1:
        result = my_list[i][0] + my_list[i][1]
        results.append(result)
    elif my_list[i][2] == 2:
        result = my_list[i][0] - my_list[i][1]
        results.append(result)
    else:
        result = my_list[i][0] * my_list[i][1]
        results.append(result)

print(results)
