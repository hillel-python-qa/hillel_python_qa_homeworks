friends = ["John", "Marta", "James"]
enemies = ["John", "Jonathan", "Artur"]

for friend in friends:
    if friend in enemies:
        print(f"{friend}  we are not the friends anymore")
    elif friends == "James":
        continue
    else:
        print(f"{friend} we are the best friends")
