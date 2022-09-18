def custom_max(collection: iter, results_count: int = 1):
    if results_count == 0:
        return []
    elif results_count == len(collection):
        return collection
    elif results_count > len(collection):
        raise Exception("Wrong results count!!!")
    max_elements = []
    for element in reversed(collection):
        if len(max_elements) < results_count:
            max_elements.append(element)
        else:
            for value in max_elements:
                if element > value:
                    max_elements[max_elements.index(value)] = element
                    break
    return max_elements


def custom_min(collection: iter, results_count: int = 1):
    if results_count == 0:
        return []
    elif results_count == len(collection):
        return collection
    elif results_count > len(collection):
        raise Exception("Wrong results count!!!")
    min_elements = []
    for element in collection:
        if len(min_elements) < results_count:
            min_elements.append(element)
        else:
            for value in min_elements:
                if element < value:
                    min_elements[min_elements.index(value)] = element
    return min_elements


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(custom_min(numbers, 0))
print(custom_max(numbers, 0))
print(custom_min(numbers, 1))
print(custom_max(numbers, 1))
print(custom_min(numbers, 2))
print(custom_max(numbers, 2))
print(custom_min(numbers, 3))
print(custom_max(numbers, 3))
print(custom_min(numbers, 4))
print(custom_max(numbers, 4))
print(custom_min(numbers, 5))
print(custom_max(numbers, 5))
print(custom_min(numbers, 6))
print(custom_max(numbers, 6))
print(custom_min(numbers, 7))
print(custom_max(numbers, 7))
print(custom_min(numbers, 8))
print(custom_max(numbers, 8))
print(custom_min(numbers, 9))
print(custom_max(numbers, 9))
print(custom_min(numbers, 10))
print(custom_max(numbers, 10))

