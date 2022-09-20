def thousand_seven():
    '''
    A function that returns a number in range from 1 to 1000 if it's dividable by 7 without a remainder
    '''
    return [number for number in range(1, 1000) if number % 7 == 0]


print(thousand_seven())


def thousand_seven_gen():
    '''
    A function that returns next number that is dividable by 7 without a remainder
    '''
    counter = 0
    while counter <= 1000:
        if counter % 7 == 0:
            yield counter
        counter += 1

for number in thousand_seven_gen():
    print(number)