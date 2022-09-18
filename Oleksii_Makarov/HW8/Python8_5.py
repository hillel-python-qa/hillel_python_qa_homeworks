def my_all(inp: list) -> bool:
    """
    Returns False if item in argument IS NOT True, otherwise returns True
    """
    for item in inp:
        if not item:
            return False
    return True


check = [1, 1, 1, 1, 1, 2, False]
check2 = []
check3 = ['David', 'Martin', 'Maine', 'Rebecca', 'Lucy', '']
print(my_all(check))
print(my_all(check2))
print(my_all(check3))
print(all(check))
print(all(check2))
print(all(check3))
