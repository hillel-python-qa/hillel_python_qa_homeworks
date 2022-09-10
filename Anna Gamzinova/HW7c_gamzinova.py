# is_prime function

def is_prime(number):
    prime = True
    if number in range(2, 1001):
        for n in range(2, int(number/2)):
            if number % n == 0:
                prime = False
                break
        return prime
    else:
        return "Number is not in range"


# print(is_prime(1))
# print(is_prime(1000))
# print(is_prime(5))
# print(is_prime(10))
# print(is_prime(19))
# print(is_prime(2))

