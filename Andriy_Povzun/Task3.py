omnivores_guests = ['John', 'Lui', 'Andy', 'Sandy', 'Cler', 'Tanya',
                    'Fitch', 'Artur', 'Susan', 'Killian']
vegetarians_guests = ['John', 'Lui', 'Andy', 'Sandy', 'Cler', 'Tanya',
                      'Fitch', 'Artur', 'Susan', 'Killian', 'Yulia',
                      'Steve', 'Gleb', 'Alex']
only_vegetarians = list(set(vegetarians_guests) - set(omnivores_guests))
print(f'This people eat only vegetarians food: {only_vegetarians}')

