# Write a function is_prime that takes 1 argument - a number from 2 to 1000,
# and returns True if it is a prime number, and False otherwise.

def is_prime(number: int) -> bool:
    if type(number) is str:
        return False
    elif 2 <= number <= 1000:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_prime(88))

