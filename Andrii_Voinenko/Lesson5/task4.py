import re

variables = ["FirstItem", "FriendsList", "MyTuple"]
snake_case = []

for variable in variables:
    snake_case.append(re.sub(r'(?<!^)(?=[A-Z])', '_', variable).lower())

print(snake_case)
