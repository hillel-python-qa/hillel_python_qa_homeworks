import re
import json

task_string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
split_task_string = str(re.split('=|&|sssss', task_string))
print("The list after performing split functionality : " + str(split_task_string))
for values in split_task_string:
    str(values).replace(' ', '')
    print(json.loads(split_task_string))

# Я не понимаю, как правильно реализовать переход от строки в словарь
