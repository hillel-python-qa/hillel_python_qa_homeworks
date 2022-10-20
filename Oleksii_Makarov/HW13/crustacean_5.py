from animal_1 import Animal
import re


class Crustacean(Animal):
    def __init__(self, reproduction: str, habitation: str, food: str, shell_color: str):
        super().__init__(habitation, reproduction)
        self._food = food
        self._shell_color = shell_color

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

    @property
    def shell_color(self):
        """
            Returns shell color name
        """
        return self._shell_color

    @shell_color.setter
    def shell_color(self, new_color):
        """
            Takes one parameter, check if it's filled and sets it's as new shell color
        """
        if re.search(r'\S', new_color):
            self._shell_color = new_color
        else:
            raise ValueError("Color must be filled")

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

    def _my_color(self):
        """
           Prints phrase using protected attribute shell_color
        """
        print(f'My shell color is {self._shell_color}')

    def color(self):
        """
            Uses protected method _my_color
        """
        self._my_color()


if __name__ == '__main__':
    crab = Crustacean('Eggs', 'Under Water', 'Everything', 'Red')
    crab.color()
    crab.living()
    crab.reproducing()
    crab.eating()
