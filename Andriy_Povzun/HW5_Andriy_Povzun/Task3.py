import re

string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
string = string.strip()
data_about_Amanda = re.sub(r'=|&+', ' ', string)
data_about_Amanda = data_about_Amanda.split(' ')
data_about_Amanda.remove('sssss')

dictionary = {}
index = 0

for element in data_about_Amanda:
    dictionary[data_about_Amanda[index]] = data_about_Amanda[index + 1]
    index += 2
    if index == len(data_about_Amanda):
        break
print(dictionary)
