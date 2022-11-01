from Oleksadr_Petrov.HW11.Mammals import Mammals


class WaterMammals(Mammals):

    def __init__(self, species: str, age: int, voice: str, food_preferences: str, pregnancy_period: float,
                 dwelling_depth: float):
        super(WaterMammals, self).__init__(species, age, voice, food_preferences, False, "Live birth", pregnancy_period,
                                           legs_count=0)
        self.__dwelling_depth = dwelling_depth

    @property
    def dwelling_depth(self):
        return self.__dwelling_depth

    @dwelling_depth.setter
    def dwelling_depth(self, dwelling_depth):
        self.__dwelling_depth = dwelling_depth

    def move(self):
        print('I\'m swim!')
