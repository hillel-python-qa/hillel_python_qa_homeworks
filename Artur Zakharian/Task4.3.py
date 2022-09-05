friends = ["John", "Marta", "James"]
enemies = ["John", "Jonathan", "Artur"]
for friend in friends:
    if friend in enemies:
        print(friend, "we are not the friends anymore")
    elif friend not in enemies and friend != "James":
        print(friend, "we are the best friends")
print('James we best friends')
