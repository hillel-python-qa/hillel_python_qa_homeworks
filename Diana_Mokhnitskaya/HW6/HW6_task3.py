import re
from collections import Counter
with open("text.txt") as file:
    new_string = file.read()
    print(new_string)
    all_characters = re.findall(r"[A-z]", new_string)
    print(Counter(all_characters))
    
