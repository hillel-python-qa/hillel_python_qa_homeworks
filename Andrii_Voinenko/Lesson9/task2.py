def range_generator():
    counter = 0
    while counter <= 1000000000:
        yield counter
        counter += 1


for number in range_generator():
    if number % 2 == 0:
        print(pow(number, 2))
