import re


def number_remove(file_name: str):
    with open(file_name, 'r') as file:
        file_content = file.read()
        updated_content = re.sub(r'\d', "", file_content)
    with open(file_name, 'w') as file:
        file.write(updated_content)


file_name = "test"
number_remove(file_name)

