def even_numbers(numbers: list):
    for number in numbers:
        if number % 2 == 0:
            return True
        else:
            return False


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(even_numbers, numbers)

print(even_numbers)
