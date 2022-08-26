casino_blacklist = ['Elena Preset', 'Matvei Lure', 'Inna Gwen', 'Alexander Mukul', 'Bogdan Mosh', 'Inna Loki']
poker_blacklist = ['Serjoscha Ikn', 'Vanya Heap', 'Bogdan Mosh', 'Elena Coup', 'Inna Gwen', 'Elena Preset']
alcohol_blacklist = ['Kristina Dew', 'Inna Gwen', 'Elena Preset', 'Bogdan Mosh', 'Oksana Joy']

print('It is not allowed to play in a casino: ')
print(casino_blacklist)
print('Not allowed to play poker: ')
print(poker_blacklist)
print('Not allowed to enter the bar : ')
print(alcohol_blacklist)

list_merged_1 = list(set(alcohol_blacklist).intersection(poker_blacklist))
list_merged_2 = list(set(casino_blacklist).intersection(list_merged_1))

print('Includes all three lists: ')
print(list_merged_2)
