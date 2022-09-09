if __name__ == "__main__":
    def calc(a, b, c):
        if c == "+":
            return a + b
        elif c == "*":
            return a * b
        elif c == "-":
            return a - b
        elif c == "/":
            return a / b
print(calc(5, 5, "/"))
