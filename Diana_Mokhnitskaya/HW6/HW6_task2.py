import pickle
import math
with open("HW_6_task3.txt", "r+b") as file:
    text = file.read()
    # print(text)
    ordinary_data = pickle.loads(text)
    # print(ordinary_data)
    result = [math.prod(tup) for tup in ordinary_data]
    print(result)
