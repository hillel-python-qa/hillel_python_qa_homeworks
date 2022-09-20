def decor(func: callable):
    def wrapper(*args):
        return f"{func.__name__}\n{func(*args)}"

    return wrapper


@decor
def sum_func(number1: int, number2: int) -> int:
    sum_result = number1 + number2
    return sum_result


@decor
def mult_func(number3: int, number4: int) -> int:
    mult_result = number3 * number4
    return mult_result


print(sum_func(5, 6))

print(mult_func(5, 6))
