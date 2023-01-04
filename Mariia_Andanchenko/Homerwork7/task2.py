from math import sqrt


def square_calculator(side: float) -> tuple:
    """
        Takes side of the square, and returns a tuple of its parameters
            (perimeter, area, diagonal)
    """
    square_perimeter = side * 4
    square_area = pow(side, 2)
    square_diagonal = round(side * sqrt(2), 2)
    return square_perimeter, square_area, square_diagonal


if __name__ == "__main__":
    square_parameters = square_calculator(3)
    print(f'Square perimeter: {square_parameters[0]}\n'
          f'Square area: {square_parameters[1]}\n'
          f'Square diagonal: {square_parameters[2]}')