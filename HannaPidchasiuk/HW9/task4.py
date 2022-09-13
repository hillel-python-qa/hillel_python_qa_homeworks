# Find all the numbers from 1-1000 that have a 3 in them
def find_have_3_inside(min_elements: int, max_elements: int) -> list:
    return [item for item in range(min_elements, max_elements) if str(item).count("3")]


def my_gen():
    counter = 1
    while counter <= 1000:
        if str(counter).count("3"):
            yield counter
        counter += 1


if __name__ == "__main__":
    print(find_have_3_inside(1, 1000))

    gen = my_gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
