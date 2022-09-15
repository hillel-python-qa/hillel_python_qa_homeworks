import re
info = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"

update_info = re.split("\W", info)
values_list = []

for element in update_info:
    if element == 'sssss':
        update_info.remove(element)
    elif element == '':
        update_info.remove(element)


for i, v in enumerate(update_info):
    if i % 2 == 1:
        values_list.append(v)


del update_info[1::2]

my_dict = dict(zip(update_info, values_list))
print(my_dict)





