def return_function_name(func: callable):
    def wrapper(*args):
        return f'The name of the function: {func.__name__}\nResult: {func(*args)}'

    return wrapper


@return_function_name
def my_sum(term1: float, term2: float):
    return term1 + term2


print(my_sum(1, 5))
