list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_list = []
even_list = []

for count, number in enumerate(list_of_elements):
    if number % 2 == 0:
        print("Even numbers:", count, number)
    else:
        print("Odd numbers:", count, number)
