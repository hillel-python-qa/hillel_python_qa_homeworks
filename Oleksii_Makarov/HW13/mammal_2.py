from animal_1 import Animal
import re


class Mammal(Animal):
    def __init__(self, reproduction: str, habitation: str, food: str):
        super().__init__(habitation, reproduction)
        self._food = food

    def _i_am_reproducing(self):
        """
            Prints phrase using protected attribute reproduction
        """
        print(f'I am reproducing using {self._reproduction}')

    def _i_eat(self):
        """
            Prints phrase using protected attribute food
        """
        print(f'I eat {self._food}')

    def _i_live(self):
        """
           Prints phrase using protected attribute habitation
        """
        print(f'I live in {self._habitation}')

    def reproducing(self):
        """
            Uses protected method _i_am_reproducing
        """
        self._i_am_reproducing()

    def eating(self):
        """
            Uses protected method _i_eat
        """
        self._i_eat()

    def living(self):
        """
            Uses protected method _i_live
        """
        self._i_live()

