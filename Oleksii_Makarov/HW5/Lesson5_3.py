before = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
after_temp = before.strip().replace('=sssss', '').split('&')
after = {}
for rest in after_temp:
    if rest.find('=') > 0:
        split_result = rest.split('=')
        after.update({split_result[0]: split_result[1]})
print(after)