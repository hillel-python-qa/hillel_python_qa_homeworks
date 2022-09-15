import re

with open('text.txt', 'r') as file:
    text = file.read()

letter_count = {}
# This regex fucntion replaces almost every dash "-" with "Ђв" and I have no idea why
# Hence telling it to also replace them. And it's working for some reason
only_letters = re.sub(r'[^a-zA-Z]', '', text)
for letter in sorted(only_letters, key=str.lower):
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
for key, value in letter_count.items():
    print(f'{key}:{value}')
