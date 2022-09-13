# Find all the numbers from 1-1000 that are divisible by 7
def find_division_by_7(min_elements: int, max_elements: int) -> list:
    return [item for item in range(min_elements, max_elements) if item % 7 == 0]


def my_gen():
    counter = 1
    while counter <= 1000:
        if counter % 7 == 0:
            yield counter
        counter += 1


if __name__ == "__main__":
    print(find_division_by_7(1, 1000))

    gen = my_gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
