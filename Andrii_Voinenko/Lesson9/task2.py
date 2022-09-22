def range_generator():
    counter = 0
    while counter <= 1000000000:
        if counter % 2 == 0:
            yield pow(counter, 2)
        counter += 1
