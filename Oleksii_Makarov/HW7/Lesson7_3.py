def is_prime(num: int) -> bool:
    """
        Takes number and returns TRUE if it's prime number in range from 2 to 1000.
        If not prime returns FALSE. If beyond the range returns "Out of range".
    """
    if num <= 1:
        return False
    elif num > 1000:
        return "Out of range"
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


print(is_prime(int(input())))
