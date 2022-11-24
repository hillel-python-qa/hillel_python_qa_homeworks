from typing import List
import re
with open("task_1.py") as file:
    prepare_file = file.read()
# print(prepare_file)
line = re.sub(r'[^\w\s]+|[\d]+', r'', prepare_file)
print(line)

# Помоги, пожалуйста, с тем, как правильно огласить функцию и переменные, которые обращаются 
# к текстовому файлу

# def delete_digits_from_strings(line: str) -> List:
#     for line in prepare_file:
#         line = re.sub(r'[^\w\s]+|[\d]+', r'', prepare_file)
#         finish_text = tuple(line)
#     print(delete_digits_from_line())
#         return finish_text
