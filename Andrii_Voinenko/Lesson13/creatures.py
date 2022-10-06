from mammals import Mammals


class Predators(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str):
        super().__init__(name, gender, health, claws, ration)

    def hunting(self):
        print(f"{self.__name} hunt on weaker animal using {self.__claws}")


class Oviparous(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str):
        super().__init__(name, gender, health, claws, ration)


class Marsupilas(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str):
        super().__init__(name, gender, health, claws, ration)


class Herbivores(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str):
        super().__init__(name, gender, health, claws, ration)


class WaterMammals(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str):
        super().__init__(name, gender, health, claws, ration)
