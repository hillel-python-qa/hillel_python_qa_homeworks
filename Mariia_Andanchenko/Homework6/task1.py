from random import randint
import os


def create_list(length):
    result_list = []
    for i in range(length):
        temp_first = randint(1, 100)
        temp_second = randint(1, 100)
        temp_action = randint(1, 3)
        result_list.append((temp_first, temp_second, temp_action))
    return result_list


if __name__ == "__main__":
    try:
        os.makedirs("data")
    except FileExistsError:
        print("ERROR file exists: 'data'")

    os.chdir("data")
    with open("task2.txt", "w") as file:
        for element in create_list(100):
            file.write(f'{element[0]} {element[1]} {element[2]}\n')