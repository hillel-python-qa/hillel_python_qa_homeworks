def generator_of_square():
    number = 0
    while number <= 1000000000:
        if number % 2 == 0:
            yield pow(number, 2)
        number += 1


if __name__ == "__main__":
    gen = generator_of_square()
    print(next(gen))
    print(next(gen))
    print(next(gen))

    for item in generator_of_square():
        print(item)
