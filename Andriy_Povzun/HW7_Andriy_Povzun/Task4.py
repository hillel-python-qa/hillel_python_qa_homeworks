import re


def number_remover(file_name: str):
    with open(file_name, 'r') as file:
        rows = file.readlines()
    file_without_numbers = []
    for row in rows:
        file_without_numbers.append(re.sub(r'\d', '', row))
    return file_without_numbers
