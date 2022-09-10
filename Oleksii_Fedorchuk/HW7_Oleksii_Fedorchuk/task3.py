"""Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is a prime number,
and False otherwise."""

if __name__ == "__main__":
    def in_prime(number: int):
        if number <= 1:
            return False
        if number >= 1002:
            return False
        if number in range(2, 1001):
            return True
        if number % 2 == 0:
            return False
        if number is not None:
            return False
print(in_prime(5))
