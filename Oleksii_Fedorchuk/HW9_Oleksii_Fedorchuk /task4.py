def squares_func():
    number = 0
    for number in range(0, 1000000001):
        if '3' in str(number):
            print(number)


print(squares_func())
