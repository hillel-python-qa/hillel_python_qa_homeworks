# Using the created file in task 1, read the file and perform mathematical operations on each element.
# Output the result of the operation to the console.
# You cannot use imports to import from the first task module.

if __name__ == "__main__":
    with open("./test/data/task2.txt") as file:
        elements = file.readlines()

    split_for_operands = []
    for element in elements:
        split_for_operands.append(element.replace("\n", "").split(" "))

    for item in split_for_operands:
        if item[2] == "1":
            print(f'{item[0]} + {item[1]} = {int(item[0]) + int(item[1])}')
        elif item[2] == "2":
            print(f'{item[0]} - {item[1]} = {int(item[0]) - int(item[1])}')
        elif item[2] == "3":
            print(f'{item[0]} * {item[1]} = {int(item[0]) * int(item[1])}')
        else:
            continue
