def is_prime(number: int) -> bool:
    if number < 2 or number > 1000:
        raise Exception('Function work with number in range from 2 to 1000')
    else:
        divided = 0
        for i in range(2, number - 1):
            if number % i == 0:
                divided += 1
                if divided > 0:
                    break
        if divided != 0:
            return False
        else:
            return True


"""
The function returns True if the number is prime, False otherwise
"""
