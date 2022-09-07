# expected result = {name: Amanda, age: 32, salary: 1500, currency: quro}
string_1 = 'name=Amanda=sssss&age=32&&salary=1500&currency=euro'
string_2 = string_1.replace('=sssss', '').replace('&&', '&').split('&')
part_1 = string_2[0].split('=')
part_2 = string_2[1].split('=')
part_3 = string_2[2].split('=')
part_4 = string_2[3].split('=')
part = part_1,  part_2,  part_3,  part_4
our_dict = {i[0]: i[1] for i in part}

print(our_dict)
print(type(our_dict))

