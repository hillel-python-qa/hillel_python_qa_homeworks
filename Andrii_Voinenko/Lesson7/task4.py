def remove_number_from_string(file_name: str):

    # Open file and take its text
    with open(file_name, "r") as file:
        text = file.read()
        without_digits = []

        # Checking if char != digit
        for char in text:
            if not char.isdigit():
                without_digits.append(char)

        # Adding all chars without digits
        result = ''.join(without_digits)

    return print(result)


remove_number_from_string("./text.txt")
