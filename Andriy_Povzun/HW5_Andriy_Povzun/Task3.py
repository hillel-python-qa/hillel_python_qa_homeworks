string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
string = string.strip()
string = string.replace('&&', '&')
string = string.replace('&', '=')
data_about_Amanda = string.split('=')
data_about_Amanda.remove('sssss')

dictionary = {}
index = 0

for times in range(int(len(data_about_Amanda) / 2)):
    dictionary[data_about_Amanda[index]] = data_about_Amanda[index + 1]
    index += 2
print(dictionary)
