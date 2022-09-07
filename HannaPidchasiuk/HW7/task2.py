# Write a function square that takes 1 argument, the side of the square, and returns 3 values
# (using a tuple): the perimeter of the square, the area of the square, and the diagonal of the square.
from math import sqrt


def square(side: float) -> tuple:
    """
        Takes side of the square, and returns a tuple of its parameters
            (perimeter, area, diagonal)
    """
    square_perimeter = side * 4
    square_area = pow(side, 2)
    square_diagonal = round(side * sqrt(2), 3)
    return square_perimeter, square_area, square_diagonal


if __name__ == "__main__":
    square_parameters = square(2)
    print(f'Square perimeter: {square_parameters[0]}\n'
          f'Square area: {square_parameters[1]}\n'
          f'Square diagonal: {square_parameters[2]}')
