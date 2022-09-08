# Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is a prime number,
# and False otherwise.

def is_prime(digit: int) -> bool:
    """
            Takes 1 argument(number) and returns TRUE if it is a prime number. Otherwise, returns FALSE.
            Range from 2 till 1000 (including).
    """
    number = max(min(digit, 1000), 2)
    count_of_loop = 0
    for i in range(2, number):
        if number % i == 0:
            count_of_loop += 1

    if count_of_loop == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print((is_prime(18)))
