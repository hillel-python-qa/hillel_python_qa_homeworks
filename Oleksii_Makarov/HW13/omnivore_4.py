from mammal_2 import Mammal
import re


class Omnivore(Mammal):
    def __init__(self, reproduction: str, habitation: str, food="everything"):
        super().__init__(reproduction, habitation, food)

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
    monkey = Omnivore('Live Birth', 'Jungle')
    monkey.reproducing()
    monkey.eating()
    monkey.living()
