friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend == 'James':
        print(f"{friend} we are the best friends")
        continue
    if friend in enemies:
        print(f"{friend} we are not the friends anymore")
    else:
        print(f"{friend} we are the best friends")