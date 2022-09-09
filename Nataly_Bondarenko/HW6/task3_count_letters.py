# Please count how many times each letter appears in this file
from collections import Counter

with open('text.txt', 'r') as file:
    data = file.read()

rep_list = ['-', '.', ' ', "'", "[", ":", '"', ']', 'â€', '”', '3', '2', ';',
            '(', ')', '\n', '7', '0', ',']

for ch in rep_list:
    if ch in data:
        data = data.replace(ch, '')

result = Counter(data)
print(result)
