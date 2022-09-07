import re

with open("text.txt", 'r') as file:
    text = file.read()

text = re.findall('[A-z]', text)
formatted_text = ''.join(text).lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = {}
for char in alphabet:
    result[char] = 0

for char in formatted_text:
    for key, value in result.items():
        if char == key:
            value = value + 1
            result[char] = value

for key, value in result.items():
    print(f'Letter "{key}" appears {value} times in this text.')
