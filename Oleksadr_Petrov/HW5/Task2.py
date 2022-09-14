names = ["John", "Marta", "James", "Amanda", "Marianna"]
header = "Names"
print(f"{header.center(21, '*')}")

for name in names:
    print(f"{name:>21}")
