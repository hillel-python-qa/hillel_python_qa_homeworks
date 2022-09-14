def my_all(sequence: list):
    for element in sequence:
        if element == (0 or '' or ""):
            return False
    return True
