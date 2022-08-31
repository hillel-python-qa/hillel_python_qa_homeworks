friends = ["John", "Marta", "James", "Jonathan", "Daniel"]
enemies = ["John", "Jonathan", "Artur", "Daniel", "Marcel"]

for person in friends:
    if person in enemies:
        print(f"{person} we are not the friends anymore")
    elif person == "James":
        continue
    else:
        print(f"{person} we are the best friends")
