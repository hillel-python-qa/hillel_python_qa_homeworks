friends = ["John", "Marta", "James"]
enemies = ["John", "Jonathan", "Artur"]
for i in friends:
    if i == "James":
        print(i, "we best friends")
    elif i in enemies:
        print(i, "we are not the friends anymore")
    else:
        print(i, "we are the best friends")
