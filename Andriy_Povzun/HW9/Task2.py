squares_of_even_numbers = (number * number for number in range(0, 1000000000) if number % 2 == 0)
if __name__ == '__main__':
    generator = squares_of_even_numbers
    for item in generator:
        print(item)
