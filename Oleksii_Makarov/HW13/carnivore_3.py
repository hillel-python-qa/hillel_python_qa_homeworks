from mammal_2 import Mammal
import re


class Carnivore(Mammal):
    def __init__(self, habitation: str, reproduction: str, food="meat"):
        super().__init__(habitation, reproduction, food)

    @property
    def habitation(self):
        """
            Return habitation name
        """
        return self._habitation

    @habitation.setter
    def habitation(self, new_habitation):
        """
            Takes one parameter, check if it's filled and sets it's as new Habitation
        """
        if re.search(r'\S', new_habitation):
            self._habitation = new_habitation
        else:
            raise ValueError("Name must be filled")

    @property
    def reproduction(self):
        """
            Returns reproduction name
        """
        return self._reproduction

    @reproduction.setter
    def reproduction(self, new_reproduction):
        """
            Takes one parameter, check if it's filled and sets it's as new Reproduction
        """
        if re.search(r'\S', new_reproduction):
            self._reproduction = new_reproduction
        else:
            raise ValueError("Name must be filled")

    @property
    def food(self):
        """
            Returns food name
        """
        return self._habitation

    @food.setter
    def food(self, new_food):
        """
            Takes one parameter, check if it's filled and sets it's as new Food
        """
        if re.search(r'\S', new_food):
            self._food = new_food
        else:
            raise ValueError("Name must be filled")


if __name__ == '__main__':
    cheetah = Carnivore("live birth", "savanna")
    cheetah.eating()
    cheetah.reproducing()
    cheetah.living()
