import re

f = open('text')
string = f.read()
update_string = re.sub(r'\.{2,}', '.', string)
update_string = re.sub(r'\b[A-Za-z]+ [A-Za-z]+\.[A-Za-z]+\.', 'The Hubble Space ', update_string)
update_string = re.sub(r'\.[A-Z]', '. A', update_string)
update_string = re.sub(r'\n', '', update_string)
list_strings = re.split(r'\b\.\s', update_string)
print(list_strings)
