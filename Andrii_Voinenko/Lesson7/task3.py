def is_prime(number_to_check: int) -> bool:
    if number_to_check > 1 and number_to_check < 1001:
        for num in range(2, number_to_check):
            if (number_to_check % num) == 0:
                return False
        return True
    else:
        return print(f"Enter number more then 2 and less than 1000")


is_prime(100)
