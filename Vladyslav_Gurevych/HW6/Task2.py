with open("test/data/result.txt", 'r') as file:
    temp = file.read()

math_expressions = temp.strip().split('\n')

for expressions in math_expressions:
    split_digit = expressions.split(' ')
    if split_digit[2] == '1':
        addition = int(split_digit[0]) + int(split_digit[1])
        print(f'The result of addition operation is {addition}')

    if split_digit[2] == '2':
        subtraction = int(split_digit[0]) - int(split_digit[1])
        print(f'The result of subtraction operation is {subtraction}')

    if split_digit[2] == '3':
        multiplication = int(split_digit[0]) * int(split_digit[1])
        print(f'The result of multiplication operation is {multiplication}')
