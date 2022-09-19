"""You have a file of unknown length. Write a function that will remove all numbers from each line of the file."""

if __name__ == "__main__":
    def calc(a: int, b: int, c: str) -> int:
        if c == "+":
            return a + b
        elif c == "*":
            return a * b
        elif c == "-":
            return a - b
        elif c == "/":
            return a / b
print(calc(5, 5, "/"))
