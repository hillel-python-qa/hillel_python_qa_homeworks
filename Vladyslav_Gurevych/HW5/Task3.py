# there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}

staff = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
staff_new = staff.lstrip().rstrip().replace("&&","&").split("&")
staff_new = " ".join(staff_new).replace("=sssss", "")
staff_new = "".join(staff_new).replace("=", " ").split(" ")
key = []
value = []
result = {}
for index, element in enumerate(staff_new):
    if index % 2 == 0:
        key.append(element)
    else:
        value.append(element)

for i in range(len(value)):
    result.update({key[i]: value[i]})
print(result)
