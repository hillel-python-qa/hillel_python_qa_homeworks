import re

REG = r"(.+?)([A-Z])"


def snake(match):
    return match.group(1).lower() + "_" + match.group(2).lower()


list_of_items = ["FirstItem", "FriendsList", "MyTuple"]
results = [re.sub(REG, snake, i, 0) for i in list_of_items]

print(results)
