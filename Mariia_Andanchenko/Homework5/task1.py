names = "john peter brian Morgan Adam Maria bart"
names_list = names.split()
new_names_list = []

for name in names_list:
    new_names_list.append(name.capitalize())

new_names = " ".join(new_names_list)
print(new_names)
