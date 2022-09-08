import math

# The function returns perimeter, area and diagonal of the square


def square(side_length):
    return 4 * side_length, side_length ** 2, side_length * math.sqrt(2)


# Printing the result in tuple
print(square(3))
