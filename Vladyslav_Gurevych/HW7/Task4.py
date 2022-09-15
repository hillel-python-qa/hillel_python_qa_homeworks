import re


def remove_numbers_from_file(file_path: str) -> list:
    """
        Takes list of lines from file and returns list of same lines without numbers.
    """
    with open(file_path, "r") as file:
        text = file.readlines()
    text_without_numbers = []
    for line in text:
        text_without_numbers.append(re.sub(r'[0-9]', "", line))
    return text_without_numbers
