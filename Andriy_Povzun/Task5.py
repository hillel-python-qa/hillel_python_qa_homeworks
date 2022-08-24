non_unique_names = ['Conor Mcgregor', 'Kamaru Usman', 'John Jones', 'Daniel Cormier',
                    'Jose Aldo', 'Conor Mcgregor', 'Jose Aldo', 'Jimmy Manuva', 'John Jones']
unique_names = []
for name in non_unique_names:
    if name not in unique_names:
        unique_names.append(name)
print(unique_names)
