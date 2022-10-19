from Project_Git.hillel_python_qa_homeworks.Oleksii_Fedorchuk.HW13_Oleksii_Fedorchuk.animal import Animal


class Mammal(Animal):
    def __init__(self):
        super().__init__("Mammal")
        print(f"Mammal is a warmblooded")
