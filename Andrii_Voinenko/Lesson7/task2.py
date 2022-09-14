import math


def square(square_side_value: float) -> tuple:
    calc_perimeter = square_side_value * 4
    calc_square_area = pow(square_side_value, 2)
    calc_diagonal = square_side_value * math.sqrt(2)
    result = (calc_perimeter, calc_square_area, round(calc_diagonal, 2))
    return result


square(15)
