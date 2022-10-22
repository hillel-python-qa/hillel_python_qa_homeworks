import random

from mammals import Mammals


class Predators(Mammals):
    def __init__(self, name: str, age: int, max_age: int, favorite_fowl: str):
        super().__init__(name, age, max_age)
        self.favorite_fowl = favorite_fowl

    @staticmethod
    def __hunt():
        return random.choice(["caught", "not catch", "not found"])

    def eat(self):
        hunt_result = self.__hunt()
        if hunt_result == "caught":
            return f"I am eating {self.favorite_fowl}"
        else:
            return f"Oh no! I do {hunt_result}"


if __name__ == '__main__':
    cat: Predators = Predators("Rysia", 3, 20, "mouses")
    print(cat.eat())
    print(cat.eat())
    print(cat.eat())
    print(cat.grow_up())
    print(cat.drink())
