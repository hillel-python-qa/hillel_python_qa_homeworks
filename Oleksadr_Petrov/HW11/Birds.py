from Oleksadr_Petrov.HW11.Animals import Animals


class Birds(Animals):

    def __init__(self, species: str, age: int, voice: str, food_preferences: str, wingspan: float):
        super(Birds, self).__init__(species, age, voice, food_preferences, fly_possibility=True,
                                    way_of_procreation="Eggs")
        self.__wingspan = wingspan

    @property
    def wingspan(self):
        return self.__wingspan

    @wingspan.setter
    def wingspan(self, wingspan):
        if wingspan <= 0:
            raise Exception("Wrong value for wingspan!")
        self.__wingspan = wingspan

    def move(self):
        print('I\'m fly!')




