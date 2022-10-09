import re
camel_list = ["FirstItem", "FriendsList", "MyTuple"]
camel_string = str(camel_list)
snake_string = re.sub(r'(?=[I-T^M])', '_', camel_string).lower()
print(snake_string)
