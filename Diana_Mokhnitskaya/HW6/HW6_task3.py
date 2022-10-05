import re
from collections import Counter
with open("text.txt") as file:
    new_string = file.read()
    print(new_string)
    all_characters = re.findall(r"[a-zA-Z]\D\S", new_string)
    print(Counter(new_string))

# Не понимаю, как убрать символы и точки из подсчета
