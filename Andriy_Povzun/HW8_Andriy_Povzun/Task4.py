def my_max(objects: list, amount_of_result=1):
    sorted_list = sorted(objects, reverse=True)
    return sorted_list[:amount_of_result]


"""
An alternative to the max() built-in function
"""


def my_min(objects: list, amount_of_result=1):
    sorted_list = sorted(objects)
    return sorted_list[:amount_of_result]


"""
An alternative to the min() built-in function
"""

if __name__ == '__main__':
    numbers = [-13.1, -2.2, -4.4, -124.1, -15.1]
    print(my_max(numbers, amount_of_result=4))
    print(my_min(numbers, amount_of_result=2))
