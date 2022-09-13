import re


def remove_all_numbers(text_file: str):
    with open(text_file, "r") as file:
        text = file.readlines()
        text_without_all_numbers = []
        for line in text:
            text_without_all_numbers.append(re.sub(r'\d', '', line))
        print(text_without_all_numbers)
