friends = ["John", "Marta", "James", "Amanda", "Marianna"]
max_name = 0
for friend in friends:
    if len(friend) > max_name:
        max_name = len(friend)

title = 'NAME'.rjust(max_name, "*")
print(f'{title}')

for name in friends:
    print(name.rjust(max_name))
