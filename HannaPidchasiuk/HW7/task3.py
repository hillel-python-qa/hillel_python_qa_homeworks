# Write a function is_prime that takes 1 argument - a number from 2 to 1000,
# and returns True if it is a prime number, and False otherwise.

def is_prime(number: float) -> bool:
    """
        Takes number and returns TRUE in case it is in range from 2 till 1000 (including).
        Otherwise, returns FALSE
    """
    if 2 <= number <= 1000:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_prime(88.5))

