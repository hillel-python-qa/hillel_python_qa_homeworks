# You have a file of unknown length.
# Write a function that will remove all numbers from each line of the file.
import re


def remove_numbers(lines: list) -> list:
    """
        Takes list of lines from file and returns list of same lines without numbers.
    """
    result = []
    for line in lines:
        result.append(re.sub(r'[0-9]', '', line))
    return result


if __name__ == '__main__':
    with open("text.txt", "r") as file:
        lines_list = remove_numbers(file.readlines())

    with open("text.txt", "w") as file:
        file.writelines(lines_list)

