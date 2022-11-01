from animals import Animals


class Mammals(Animals):
    def __init__(self, name: str, age: int, max_age: int):
        self.name = name
        self.__age = age
        self.__max_age = max_age

    def grow_up(self):
        self.__age += 1
        if self.__age >= self.__max_age:
            return self.__die()
        else:
            return self.__age

    @staticmethod
    def __die():
        return "I died("

    def eat(self):
        return f"I am eating"

    def drink(self):
        return "I am drinking water"

    def go_walk(self):
        return "I go for a walk"
