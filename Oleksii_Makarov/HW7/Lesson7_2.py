from math import sqrt


def square_calculator(side: int) -> tuple:
    square_perimeter = side * 4
    square_area = pow(side, 2)
    suqare_diagonal = round(side * sqrt(2), 2)
    return square_perimeter, square_area, suqare_diagonal


if __name__ == "__main__":
    result = square_calculator(int(input("Enter side of the square ")))
    print(result)

