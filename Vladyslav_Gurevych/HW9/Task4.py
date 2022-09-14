# Find all of the numbers from 1-1000 that have a 3 in them
def contains_3():
    number = 1
    while number <= 1000:
        if str(number).count('3'):
            yield number
        number += 1


if __name__ == "__main__":
    gen = contains_3()
    print(next(gen))
    print(next(gen))
    print(next(gen))

    for item in contains_3():
        print(item)

    numbers_contains_3 = [item for item in range(1, 1000) if str(item).count('3')]
    print(numbers_contains_3)
