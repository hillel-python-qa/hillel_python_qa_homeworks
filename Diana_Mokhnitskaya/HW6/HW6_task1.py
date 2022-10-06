import os
import random
import pickle
os.makedirs('test/data')
a = [(random.randrange(0, 100), random.randrange(0, 100), random.randrange(0, 4)) for i in range(100)]
print(a)
with open("HW_6_task3.txt", 'r+b') as new_doc:
    text = pickle.dumps(a)
    new_doc.write(text)

with open("HW_6_task3.txt", 'r+b') as file:
    byte_text = file.read()
    print(byte_text)
