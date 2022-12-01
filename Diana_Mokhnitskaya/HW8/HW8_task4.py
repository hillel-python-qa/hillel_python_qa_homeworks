def min_function(arg):
    minimum = arg[0]
    for i in arg[1:]:
        if i < minimum:
            minimum = i
    return minimum


print(min_function([9. -6, 0, 89, 34, 1, -92]))


def max_fuction(arg_max):
    maximum = arg_max[0]
    for i in arg_max[1:]:
        if i > maximum:
            maximum = i
    return maximum


print(max_fuction([3, 76, 9, 43, 325]))
