def even_square_gen():
    '''
    Function returns a square of next even element
    '''
    counter = 0
    while counter <= 1000000000:
        if counter % 2 == 0:
            yield pow(counter, 2)
        counter += 1


# While it didn't crash it sure is made my computer loud
for number in even_square_gen():
    print(number)
