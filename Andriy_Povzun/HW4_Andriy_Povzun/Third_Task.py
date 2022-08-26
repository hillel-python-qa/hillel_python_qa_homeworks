friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend == 'James':
        continue
    elif friend in enemies:
        print(f'We with {friend} are not the friends anymore')
    else:
        print(f'We with {friend} best friends')
