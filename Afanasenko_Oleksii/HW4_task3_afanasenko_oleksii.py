friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for friend in friends:
    if friend not in enemies and friend != 'James':
        print(f'{friend} we are best friend')
    elif friend in enemies:
        print(f'{friend} we are not the friends anymore')
