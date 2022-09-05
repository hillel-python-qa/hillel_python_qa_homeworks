original_string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
convert_string = original_string.strip().replace("&&", "&").replace("=sssss", "")
dictionary = {}
#convert_string.split("&")
splited_string = convert_string.split("&")
for substring in splited_string:
    k, v = substring.split("=")
    dictionary[k] = v

print(dictionary)
