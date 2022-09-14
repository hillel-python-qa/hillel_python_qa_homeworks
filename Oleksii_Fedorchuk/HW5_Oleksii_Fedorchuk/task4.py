import re

if __name__ == "__main__":
    camel_case = ["FirstItem", "FriendsList", "MyTuple"]
    snake_case = []
    for items in camel_case:
        case = re.findall("\B[A-Z]", items)
        for same in case:
            snake_case.append(items.replace(same, f'_{same.lower()}').lower())
    print(snake_case)
