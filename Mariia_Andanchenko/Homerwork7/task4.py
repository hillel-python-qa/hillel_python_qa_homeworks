import re


def remove_numbers(file_path: str) -> list:
    """
        Takes file path and returns list of lines from file without numbers.
    """
    with open(file_path, "r") as temp_file:
        lines = temp_file.readlines()
    result = []
    for line in lines:
        result.append(re.sub(r'[0-9]', '', line))
    return result


if __name__ == '__main__':
    print(remove_numbers("text.txt"))
