def squares_of_even_elements():
    counter = 0
    while counter <= 1000000000:
        if counter % 2 == 0:
            yield counter
        counter += 1


if __name__ == "__main__":
    element = squares_of_even_elements()
    print(next(element))
    print(next(element))
    print(next(element))
