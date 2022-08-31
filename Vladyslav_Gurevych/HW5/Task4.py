# you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]

camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snake_format = []
part1 = []
part2 = []
str_camel_case = "".join(camel_case)
upper_case = str_camel_case.upper()
temple = ""
sss = "abcdefghijklmnopqrstuvwxyz"

for i in str_camel_case:
    if i in sss:
        temple += i
    else:
        temple += " " + i
temple = temple.lower().lstrip().split(" ")

for index, element in enumerate(temple):
    if index % 2 == 0:
        part1.append(element)
    else:
        part2.append(element)

for i in range(len(part1)):
    snake_format.append(part1[i] + "_" + part2[i])

print(snake_format)



