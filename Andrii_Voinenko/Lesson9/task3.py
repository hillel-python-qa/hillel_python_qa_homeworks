def range_generator():
    counter = 0
    while counter <= 1000:
        yield counter
        counter += 1


if __name__ == '__main__':
    result = [number for number in range_generator() if number % 7 == 0]
