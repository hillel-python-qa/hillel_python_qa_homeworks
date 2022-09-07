import re

values = ["FirstItem", "FriendsList", "MyTuple"]
for value in values:
    print(re.split("([a-z])([A-Z])'", value))

