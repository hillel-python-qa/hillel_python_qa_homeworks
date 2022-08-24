casino_blacklist = ['Mike Tyson', 'George Forman', 'Muhammad Ali',
                    'Dru Dober', 'Conor McGregor', 'Johny Depp']

poker_blacklist = ['Kamaru Usman', 'John Dodson', 'Tyson Fury',
                   'Johny Depp', 'Conor McGregor', 'Bradly Cooper']

alcohol_blacklist = ['Mike Tyson', 'Conor McGregor', 'Tyson Fury',
                     'Johny Depp', 'Tony Ferguson', 'Dana White']

all_blacklist = list(set(casino_blacklist) & set(poker_blacklist) & set(alcohol_blacklist))
print(f'This humans in all blacklists: {all_blacklist}')
