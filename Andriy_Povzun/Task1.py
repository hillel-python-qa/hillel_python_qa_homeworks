employees_eleks = ['John Jones', 'Andy Ruis', 'Oleksandr Usyk',
                   'Andrii Yevtushenko', 'Will Smith', 'Conor McGregor']
employees_toshiba = ['Dana White', 'Kamaru Usman', 'George St-Pierre',
                     'John Jones', 'Antony Joshua', 'Muhammad Ali']
employees_toshiba.extend(employees_eleks)
employees_eleks.clear()
print(employees_toshiba)

