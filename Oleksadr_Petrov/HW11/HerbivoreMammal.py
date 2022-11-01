from Oleksadr_Petrov.HW11.Mammals import Mammals


class HerbivoreMammal(Mammals):

    def __init__(self, species: str, age: int, voice: str, pregnancy_period: float,
                 legs_count: int, dangerous_predators: list):
        super(HerbivoreMammal, self).__init__(species, age, voice, 'Plants', False, "Live birth",
                                               pregnancy_period,
                                               legs_count)
        self.__dangerous_predators = dangerous_predators

    @property
    def dangerous_predators(self):
        return self.__dangerous_predators

    @dangerous_predators.setter
    def dangerous_predators(self, dangerous_predators):
        self.__dangerous_predators = dangerous_predators

    def move(self):
        print('I\'m move like Mammal Herbivore!')
