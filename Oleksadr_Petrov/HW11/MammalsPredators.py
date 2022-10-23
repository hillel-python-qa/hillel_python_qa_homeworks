from Oleksadr_Petrov.HW11.Mammals import Mammals


class MammalsPredators(Mammals):

    def __init__(self, species: str, age: int, voice: str, pregnancy_period: float,
                 legs_count: int, hunting_time: str):
        super(MammalsPredators, self).__init__(species, age, voice, 'Another mammals', False, "Live birth",
                                               pregnancy_period,
                                               legs_count)
        self.__hunting_time = hunting_time

    @property
    def hunting_time(self):
        return self.__hunting_time

    @hunting_time.setter
    def hunting_time(self, hunting_time):
        self.__hunting_time = hunting_time

    def move(self):
        print('I\'m move like Mammal Predator!')
