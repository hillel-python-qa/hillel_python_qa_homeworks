from mammals import Mammals


class Predators(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str, sound: str):
        super().__init__(name, gender, health, claws, ration)
        self.__sound = sound

    def hunting(self):
        print(f"{self._name} hunt on weaker animal using {self.__claws}")

    def make_noise(self):
        print(f'{self._name} makes {self.__sound} sound')


class Oviparous(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str, sound: str):
        super().__init__(name, gender, health, claws, ration)
        self.__sound = sound

    def make_noise(self):
        print(f'{self._name} makes {self.__sound} sound')


class Marsupilas(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str, sound: str):
        super().__init__(name, gender, health, claws, ration)
        self.__sound = sound

    def make_noise(self):
        print(f'{self._name} makes {self.__sound} sound')


class Herbivores(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str, sound: str):
        super().__init__(name, gender, health, claws, ration)
        self.__sound = sound

    def make_noise(self):
        print(f'{self._name} makes {self.__sound} sound')


class WaterMammals(Mammals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str, sound: str):
        super().__init__(name, gender, health, claws, ration)
        self.__sound = sound

    def make_noise(self):
        print(f'{self._name} makes {self.__sound} sound')


if __name__ == '__main__':
    wale = WaterMammals('Wale', 'Male', 'bad', False, 'plancton', 'wiiiiii')
    wale.creature_mating()
    wale.make_noise()
