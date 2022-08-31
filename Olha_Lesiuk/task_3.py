friends = ["John", "Marta", "James"]
enemies = ["John", "Jonathan", "Artur"]
for friend in friends[:2]:
    if friend not in enemies:
        print(f"{friend} we are the best friends")
    else:
        print(f"{friend} we are not friends anymore")
