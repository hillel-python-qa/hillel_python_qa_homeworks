import re


def remove_numbers_from_file(text_with_digits: list) -> list:
    """
        Takes list of lines from file and returns list of same lines without numbers.
    """
    text_without_numbers = []
    for line in text_with_digits:
        text_without_numbers.append(re.sub(r'[0-9]', "", line))
    return text_without_numbers


if __name__ == '__main__':
    with open("example.txt", "r") as file:
        text = remove_numbers_from_file(file.readlines())

    with open("example.txt", "w") as file:
        file.writelines(text)
