import math


def sqr_investigate(edge: float):
    if edge <= 0:
        raise Exception("Wrong value!!!")
    perimeter = edge*4
    area = edge ** 2
    diagonal = edge * math.sqrt(2)
    return perimeter, area, diagonal




