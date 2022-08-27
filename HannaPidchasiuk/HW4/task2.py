# You have the number 2 as a variable.
# Multiply it by 2 in two ways.
# Accordingly, you need to divide it in 2 different ways by 2.

if __name__ == "__main__":
    a = 2
    print(f'multiply 2 by 2: {a * 2}')
    print(f'multiply 2 by 2: {a << 1}')
    print(f'division 2 by 2: {a / 2}')
    print(f'division 2 by 2: {a >> 1}')
