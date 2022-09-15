# Create a decorator that prints to the console the name of the function that was called.
# The function should work as intended.

def return_name_of_func(func: callable):
    def wrapper(num_1: float, num_2: float):
        return f'Result of {func.__name__} function is {func(num_1, num_2)}'

    return wrapper


@return_name_of_func
def sum_num(num_1: float, num_2: float) -> float:
    return num_1 + num_2


@return_name_of_func
def multiply_num(num_1: float, num_2: float) -> float:
    return num_1 * num_2


if __name__ == "__main__":
    print(sum_num(2, 3))
    print(multiply_num(2, 3))
