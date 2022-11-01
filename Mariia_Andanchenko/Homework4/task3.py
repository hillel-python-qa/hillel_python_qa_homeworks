friends = ["John", "Marta", "James", "Artur", "Itan"]
enamies = ["John", "Johnatan", "Artur", "James"]

for friend in friends:
    if friend == "James":
        continue
    elif friend in enamies:
        print(f"{friend} we are not the friends anymore")
    else:
        print(f"{friend} we are the best friends")
