class Animal:
    def __init__(self, name):
        print(f"Animal type is a {name}")


class Mammal(Animal):
    def __init__(self):
        super().__init__("Mammal")
        print(f"Mammal is a warmblooded")


class Water(Mammal):
    def __init__(self):
        super().__init__()
        print(f"Water mammal is living in water\n")


class Flying(Mammal):
    def __init__(self):
        super().__init__()
        print(f"Flying mammal can fly\n")


class Predator(Mammal):
    def __init__(self):
        super().__init__()
        print(f"Mammal predator is hunting\n")


if __name__ == "__main__":
    dolphin = Water()
    bat = Flying()
    tiger = Predator()
