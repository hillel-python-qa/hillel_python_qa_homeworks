# you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
import re

if __name__ == "__main__":
    names_camel = ["FirstItem", "FriendsList", "MyTuple"]
    names_snake = []
    for name in names_camel:
        temp1 = re.findall("\B[A-Z]", name)
        for match in temp1:
            names_snake.append(name.replace(match, f'_{match.lower()}').lower())
    print(names_snake)
