def squares_func():
    number = 0
    while number <= 1000000001:
        if number % 2 == 0:
            yield number ** 2
        number += 1
        print(number)


for even_numbers in squares_func():
    print(even_numbers)
