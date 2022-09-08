friends = ["John", "Marta", "James", "Amanda", "Marianna"]
print(f'Names'.center(20, "*"))
for name in friends:
    print(f'{name.rjust(20)}')
