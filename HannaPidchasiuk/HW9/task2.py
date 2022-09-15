# Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive.
# The solution should work and not freeze your computer.


def my_gen():
    counter = 0
    while counter <= 1000000000:
        if counter % 2 == 0:
            yield pow(counter, 2)
        counter += 1


if __name__ == "__main__":
    gen = my_gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
