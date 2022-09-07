friends = ['John', 'Marta', 'James', 'Amanda', 'Marianna']
title = 'Names'

print(title.center(50, '*'))
for friend in friends:
    print(f'{friend.rjust(50)}\n')
