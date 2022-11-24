from typing import Tuple, List
import math


def square(side: int) -> Tuple[int]:
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    result = [perimeter, area, diagonal]
    return result

print(square(3))
