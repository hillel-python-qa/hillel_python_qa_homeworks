# you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8].
# Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples
# where the first element is the index and the second is the value. [(index, value)].
# accordingly, elements with an even index are placed in another list of tuples
# with the same format as in the case with odd indices.

def create_tuple_pair(arg1, arg2):
    return arg1, arg2


if __name__ == "__main__":
    my_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    even_arr, odd_arr = [], []
    for index, element in enumerate(my_arr):
        if index % 2 == 0:
            even_arr.append(create_tuple_pair(index, element))
        else:
            odd_arr.append(create_tuple_pair(index, element))

    print(f'Even pairs {even_arr}\n'
          f'Odd pairs {odd_arr}')
