def function_name(function: callable) -> callable:
    def wrapper(x, y) -> str:
        return f'{function.__name__}: {function(x,y)}'
    return wrapper


@function_name
def multiply(x: float, y: float) -> float:
    return x * y


@function_name
def addition(x: float, y: float) -> float:
    return x + y


@function_name
def subtraction(x: float, y: float) -> float:
    return x - y


@function_name
def division(x: float, y: float) -> float:
    if y == 0:
        raise Exception("Division by 0 is not supported")
    return x / y


print(multiply(4, 5))
print(division(4, 5))
print(subtraction(4, 5))
print(addition(4, 5))

