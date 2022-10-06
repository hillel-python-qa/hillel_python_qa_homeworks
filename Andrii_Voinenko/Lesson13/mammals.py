from animal import Animals


class Mammals(Animals):
    def __init__(self, name: str, gender: str, health: str, claws: bool, ration: str):
        super().__init__(name, gender, health)
        self.__claws = claws
        self.__ration = ration

    def feed_baby(self):
        if self.__feeding:
            print(f'The {self.__name} can feed its baby')

    def creature_ration(self):
        if self.__claws and self.__ration == 'meat':
            print(f'{self.__name} hunting on weaker than it animals and eat them')
        elif self.__ration == 'vegan' or 'omnivorous':
            print(f'{self.__name} could eat berries and other vegan food')

