# Convert string to a dictionary
string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
rep = string.replace('=sssss&', ' ')
rep1 = rep.replace('&&', ' ')
rep2 = rep1.replace('&', ' ')

dictionary = dict(subString.split("=") for subString in rep2.split(" "))

print(f'Dictionary :  {dictionary}')
