import re

values = ["FirstItem", "FriendsList", "MyTuple"]
result = []
for value in values:
    buffer = re.findall('[A-Z][a-z]*', value)
    result.append(buffer[0].lower() + '_' + buffer[1].lower())
print(result)

