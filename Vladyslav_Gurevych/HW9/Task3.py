# Find all of the numbers from 1-1000 that are divisible by 7
def divisible_by_7():
    number = 1
    while number <= 1000:
        if number % 7 == 0:
            yield number
        number += 1


if __name__ == "__main__":
    gen = divisible_by_7()
    print(next(gen))
    print(next(gen))
    print(next(gen))

    for item in divisible_by_7():
        print(item)

    numbers_divisible_by_7 = [item for item in range(1, 1000) if item % 7 == 0]
    print(numbers_divisible_by_7)
