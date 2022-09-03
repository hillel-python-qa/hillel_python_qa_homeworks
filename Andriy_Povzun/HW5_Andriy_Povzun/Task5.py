import re

with open('text', 'r') as file:
    text = file.read()
update_text = re.sub(r'\.{2,}', '.', text)
update_text = re.sub(r'\b[A-Za-z]+ [A-Za-z]+\.[A-Za-z]+\.', 'The Hubble Space ', update_text)
update_text = re.sub(r'\.[A-Z]', '. A', update_text)
update_text = re.sub(r'\n', '', update_text)
list_strings = re.split(r'\b\.\s', update_text)
print(list_strings)
