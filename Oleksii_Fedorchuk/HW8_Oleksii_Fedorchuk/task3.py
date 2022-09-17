list_of_numbers = [1, 2, 3, 4]
new_list_of_numbers = []

if __name__ == "__main__":
    def map_func(number: int) -> int:
        for numbers in list_of_numbers:
            new_list_of_numbers.append(numbers + 1)
        return new_list_of_numbers

print(map_func(new_list_of_numbers))
