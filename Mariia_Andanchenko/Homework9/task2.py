def gen_squares_even_elements():
    counter = 0
    while counter <= 1000000000:
        if counter % 2 == 0:
            yield counter ** 2
        counter += 1


generator = gen_squares_even_elements()

for item in generator:
    print(item)
