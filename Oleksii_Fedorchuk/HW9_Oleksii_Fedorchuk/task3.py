def squares_func():
    number = 0
    for number in range(0, 1000000001):
        if number % 7 == 0:
            print(number)


print(squares_func())
