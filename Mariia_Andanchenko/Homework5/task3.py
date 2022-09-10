text = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
text = text.strip()
params = text.split('&')
pairs = {}
for param in params:
    if param:
        values = param.split('=')
        key = values[0]
        value = values[1]
        pairs[key] = value
print(pairs)