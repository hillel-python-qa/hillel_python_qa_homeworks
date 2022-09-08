import math


def calculate_square(side_square: int) -> tuple:
    perimeter_square = side_square * 4
    diagonal_square = side_square * math.sqrt(2).round(2)
    area_square = math.sqrt(side_square)
    return perimeter_square, diagonal_square.round(2), area_square.round(2)


"""
The function returns the perimeter, diagonal, area of square, from the specified length of one side
"""
