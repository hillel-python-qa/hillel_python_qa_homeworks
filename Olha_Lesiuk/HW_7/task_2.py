def square(x):
    return x**2, x*4


a, b = square(int(input()))
print(str(a) + "is area", str(b) + "is perimeter")
