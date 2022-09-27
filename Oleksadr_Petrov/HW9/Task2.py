def squares():
    for index in range(0, 1000000000, 2):
        yield pow(index, 2)


for index in squares():
    print(index)
