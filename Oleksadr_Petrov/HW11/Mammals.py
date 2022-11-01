from Oleksadr_Petrov.HW11.Animals import Animals


class Mammals(Animals):

    def __init__(self, species: str, age: int, voice: str, food_preferences: str, pregnancy_period: float,
                 legs_count: int):
        super(Mammals, self).__init__(species, age, voice, food_preferences, fly_possibility=False,
                                      way_of_procreation="Live birth")
        self.__pregnancy_period = pregnancy_period
        self.__legs_count = legs_count

    @property
    def pregnancy_period(self):
        return self.__pregnancy_period

    @pregnancy_period.setter
    def pregnancy_period(self, pregnancy_period):
        if pregnancy_period <= 0:
            raise Exception("Wrong value for pregnancy_period!")
        self.__pregnancy_period = pregnancy_period

    @property
    def legs_count(self):
        return self.__legs_count

    @legs_count.setter
    def legs_count(self, legs_count):
        if legs_count <= 0:
            raise Exception("Wrong value for legs_count!")
        self.__legs_count = legs_count

    def move(self):
        print('I\'m move like Mammal!')
