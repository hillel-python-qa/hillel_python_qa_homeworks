from Project_Git.hillel_python_qa_homeworks.Oleksii_Fedorchuk.HW13_Oleksii_Fedorchuk.mammal import Mammal


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
