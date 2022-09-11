friends_list = ["John", "Marta", "James"]
enemies_list = ["John", "Johnatan", "Artur"]
for friend in friends_list:
    if friend == "James":
        break
    if friend not in enemies_list:
        print(f"{friend} we are the best friends"),
    else:
        print(f"{friend} we are not the friends anymore")
print("James is my best friend")
for enemy in enemies_list:
    if enemy not in friends_list:
        print(f"{enemy} we are not the friends anymore"),
    else:
        print(f"{enemy} we are the best friends")
    if enemy == "James":
        print("James is my best friend")
