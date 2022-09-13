import math


def square(side_of_square):
    perimeter_of_square = side_of_square * 4
    area_of_square = side_of_square ** 2
    diagonal_of_square = side_of_square * math.sqrt(2)
    return perimeter_of_square, area_of_square, diagonal_of_square


values = square(100)
print(f"The perimeter of the square is: {values[0]}",
      f"The area of the square is: {values[1]}",
      f"The diagonal of the square is: {values[2]}")
