from math import sqrt


def is_prime(number: int):
    for i in range(2, int(sqrt(number)) + 1):
        if (number % i) == 0:
            return True
        elif 2 <= number >= 1000:
            return None
        else:
            return False


print(is_prime(11))
