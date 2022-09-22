def my_max(item: iter) -> iter:
    """
    Reverse sorts a list and returns first position
    """
    maxi = sorted(item, reverse=True)
    return maxi[0]


def my_min(item: iter) -> iter:
    """
    Sorts a list and returns first position
    """
    mini = sorted(item, reverse=False)
    return mini[0]


names = ['David', 'Martin', 'Maine', 'Rebecca', 'Lucy']
numbers = [1, 4, 2, 6, 1, 55, 2, 61, 3, 632, -4, 3, 6655.4]
print(my_min(names))
print(my_max(names))
print(my_max(numbers))
print(my_min(numbers))
