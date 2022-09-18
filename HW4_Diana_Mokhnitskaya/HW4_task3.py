friends_list = ["John", "Marta", "James"]
enemies_list = ["John", "Johnatan", "Artur"]
for friend in friends_list:
    if friend == "James":
        print("James is my best friend")
    elif friend not in enemies_list:
        print(f"{friend} we are the best friends"),
    else:
        print(f"{friend} we are not the friends anymore")

for enemy in enemies_list:
    if enemy not in friends_list:
        print(f"{enemy} we are not the friends anymore"),
    elif enemy == "James":
        print("James is my best friend")
    else:
        print(f"{enemy} we are the best friends")

