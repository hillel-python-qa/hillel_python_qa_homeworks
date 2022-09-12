import re
import string

path = "text.txt"
letters = string.ascii_lowercase
file_content = string

with open(path, 'r') as file:
    file_content = file.read().lower()

result = {}
for letter in letters:
    letter_count = file_content.count(letter)
    result[letter] = letter_count
print(result)

