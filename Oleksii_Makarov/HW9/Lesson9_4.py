def find_three():
    '''
    Function returns every number for 1 to 1000 containing three in it
    '''
    return [number for number in range(1, 1000) if str(number).count('3')]


print(find_three())


def find_three_gen():
    '''
    Function returns next number containing a three in it
    '''
    counter = 0
    while counter <= 1000:
        if str(counter).count('3'):
            yield counter
        counter += 1


for number in find_three_gen():
    print(number)
