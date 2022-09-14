string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
remove_amp = string.strip().split('&')
result = {}
for element in remove_amp:
    buffer = element.split('=')
    if len(buffer) > 1:
        result[buffer[0]] = buffer[1]


print(result)
