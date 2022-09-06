import math


def calculate_square(side_square: int):
    perimeter_square = side_square * 4
    diagonal_square = side_square * math.sqrt(2).__round__(2)
    area_square = math.sqrt(side_square)
    tuple_results = (perimeter_square, diagonal_square.__round__(2), area_square.__round__(2))
    return tuple_results
