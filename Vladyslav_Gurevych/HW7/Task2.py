from math import sqrt


def get_square_parameters(side_of_square: float) -> tuple:
    """
        Takes side of the square, and returns a tuple of perimeter, area, diagonal
    """
    perimeter = round(side_of_square * 4, 2)
    area = round(side_of_square ** 2)
    diagonal = round(sqrt(2) * side_of_square, 2)
    return perimeter, area, diagonal


if __name__ == "__main__":
    parameters = get_square_parameters(10)
    print(f'Square perimeter is {parameters[0]}\n'
          f'Square area is {parameters[1]}\n'
          f'Square diagonal is {parameters[2]}')
