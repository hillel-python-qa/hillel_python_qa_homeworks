import re

camel_case = ["FirstItem", "FriendsList", "MyTuple"]

snake_case = []
for word in camel_case:
    result = re.findall(r'\B[A-Z]', word)
    for found in result:
        snake_case.append(word.replace(found, f'_{found}').lower())
print(snake_case)
