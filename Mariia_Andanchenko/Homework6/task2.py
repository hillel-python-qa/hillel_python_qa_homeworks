if __name__ == "__main__":
    with open("./data/task2.txt") as file:
        elements = file.readlines()
    items_list = []

    for element in elements:
        items_list.append(element.replace("\n", "").split(" "))

    for item in items_list:
        if item[2] == "1":
            print(f'{item[0]} + {item[1]} = {int(item[0]) + int(item[1])}')
        elif item[2] == "2":
            print(f'{item[0]} - {item[1]} = {int(item[0]) - int(item[1])}')
        elif item[2] == "3":
            print(f'{item[0]} * {item[1]} = {int(item[0]) * int(item[1])}')
        else:
            continue
