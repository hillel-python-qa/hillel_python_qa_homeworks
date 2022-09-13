names_friends = ["John", "Marta", "James"]
names_enamies = ["John", "Johnatan", "Artur"]
for i in names_friends:
    if i == "James":
        break
    elif i != names_enamies[0] and i != names_enamies[1] and i != names_enamies[2]:
        print(f'{i} - we are the best friend')
    else:
        print(f'{i} - we are not the friends anymore')
