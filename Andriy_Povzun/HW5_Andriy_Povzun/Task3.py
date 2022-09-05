import re

string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
string = string.strip()
data_about_amanda = re.sub(r'=s+&|=|&+', ' ', string)
data_about_amanda = data_about_amanda.split(' ')

dictionary = {}
index = 0

for element in data_about_amanda:
    dictionary[data_about_amanda[index]] = data_about_amanda[index + 1]
    index += 2
    if index == len(data_about_amanda):
        break
print(dictionary)
