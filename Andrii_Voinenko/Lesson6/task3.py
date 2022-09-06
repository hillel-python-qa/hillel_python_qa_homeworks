import re

with open('./text.txt', 'r') as file:
    text = file.read()

    all_chars = re.findall("[A-Z]|[a-z]", text)
    result = {}

    for char in all_chars:
        result[char] = all_chars.count(char)

    print(result)
