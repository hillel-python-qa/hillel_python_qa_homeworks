"""Write a function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple): the
 perimeter of the square, the area of the square, and the diagonal of the square."""

if __name__ == "__main__":
    def calculating(side):
        perimeter = side * 4
        sqr = side ** 2
        diagonal = round((2 * side ** 2) ** .5, 2)
        result = (perimeter, sqr, diagonal)
        return result
print(f"{calculating(5)}")
