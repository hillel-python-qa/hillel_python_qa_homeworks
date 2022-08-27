friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend in enemies:
        print(f"We with {friend} are not the friends anymore")
    elif friend == "James":
        continue
    else:
        print(f"We with {friend} best friends")

