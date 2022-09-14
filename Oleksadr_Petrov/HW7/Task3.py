def is_prime(value: int):
    if value < 2 or value > 1000 or type(value) != int:
        raise Exception("Wrong value")
    for index in range(value-1, 2, -2):
        if value % index == 0:
            return False
    return True
