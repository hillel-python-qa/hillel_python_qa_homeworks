def is_prime(num: int):
    if (1 >= num) or (num > 1000):
        return "Out of range"
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


print(is_prime(1))
print(is_prime(3))
print(is_prime(10))
print(is_prime(13))
print(is_prime(11232))
