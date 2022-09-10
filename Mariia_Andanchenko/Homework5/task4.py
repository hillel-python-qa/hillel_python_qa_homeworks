import re

names_old = ["FirstITem", "FriendsList", "MyTuple"]
new_names_list = []

for name in names_old:
    new_name = re.sub('(.)([A-Z])', r'\1_\2', name)
    new_name = re.sub('([A-Z])([A-Z])', r'\1_\2', new_name).lower()
    new_names_list.append(new_name)

print(new_names_list)
