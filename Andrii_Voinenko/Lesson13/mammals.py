from abc import ABC, abstractmethod
from animal import Animals


class Mammals(Animals, ABC):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str):
        super().__init__(name, gender, health)
        self.__claws = claws
        self.__ration = ration

    def feed_baby(self):
        if self._feeding:
            print(f'The {self._name} can feed its baby')

    def creature_ration(self):
        if self.__claws and self.__ration == 'meat':
            print(f'{self._name} hunting on weaker than it animals and eat them')
        elif self.__ration == 'vegan' or 'omnivorous':
            print(f'{self._name} could eat berries and other vegan food')

    @abstractmethod
    def make_noise(self):
        pass
