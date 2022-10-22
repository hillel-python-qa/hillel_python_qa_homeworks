from mammals import Mammals


class Herbivores(Mammals):
    def __init__(self, name: str, age: int, max_age: int, favorite_herb: str):
        super().__init__(name, age, max_age)
        self.favorite_herb = favorite_herb

    def eat(self):
        return f"I am eating {self.favorite_herb}"


if __name__ == '__main__':
    hamster = Herbivores("Harry", 1, 5, "mint")
    print(hamster.grow_up())
    print(hamster.eat())
    print(hamster.drink())
    print(hamster.grow_up())
    print(hamster.grow_up())
    print(hamster.grow_up())
    print(hamster.grow_up())
