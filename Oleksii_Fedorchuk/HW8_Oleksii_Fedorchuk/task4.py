list_of_numbers = [1, 45, 4, 3, 65, 37, 33]

if __name__ == "__main__":

    def max_check(numer: int) -> int:
        max_value = numer[0]
        for check in numer:
            if check > max_value:
                max_value = check
        return max_value


    def min_check(numer: int) -> int:
        min_value = numer[0]
        for check in numer:
            if check < min_value:
                min_value = check
        return min_value

print("Maximum value in the list is:", max_check(list_of_numbers))
print("Minimum value in the list is", min_check(list_of_numbers))
