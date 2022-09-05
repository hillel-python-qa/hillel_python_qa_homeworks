# 1. Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
# a. element is an integer that will be the left operand of the expression
# b. element is an integer that will be the right operand of the expression
# c. element is an integer from 1 to 3 where:
#       identifies the addition operation
#       identifies the subtraction operation
#       identifies the multiplication operation
# d. You can put data into a text file with the text form or use the pickle module in binary form.
#   If placed as text then each line should contain only elements of one tuple
#   separated by spaces (eg "100 2 3"). The file must be created by a script in
#   a pre-created \test\data directory tree. The directory tree must be created by the script.
# Push only the code to the repository (not directories or file).
from random import randint
import os


def create_list(length):
    result_list = []
    for i in range(length):
        temp_first = randint(1, 20)
        temp_second = randint(1, 20)
        temp_action = randint(1, 3)
        result_list.append((temp_first, temp_second, temp_action))
    return result_list


if __name__ == "__main__":
    try:
        os.makedirs("test/data")
    except FileExistsError:
        print("ERROR file exists: 'test/data'")

    os.chdir("test/data")
    with open("task2.txt", "w") as file:
        for i_tuple in create_list(100):
            file.write(f'{i_tuple[0]} {i_tuple[1]} {i_tuple[2]}\n')
