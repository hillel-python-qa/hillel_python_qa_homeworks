def my_own_print_function(*any_data):
    print("" + " ".join(map(str, any_data)))


my_own_print_function("Another view to print function.", 5+26)
