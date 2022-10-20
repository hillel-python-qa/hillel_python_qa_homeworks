from animal_1 import Animal
import re


class Crustacean(Animal):
    def __init__(self, reproduction: str, habitation: str, food: str, shell_color: str):
        super().__init__(habitation, reproduction)
        self._food = food
        self._shell_color = shell_color

    @property
    def habitation(self):
        return self._habitation

    @habitation.setter
    def habitation(self, new_habitation):
        if re.search(r'\S', new_habitation):
            self._habitation = new_habitation
        else:
            raise ValueError("Name must be filled")

    @property
    def reproduction(self):
        return self._reproduction

    @reproduction.setter
    def reproduction(self, new_reproduction):
        if re.search(r'\S', new_reproduction):
            self._reproduction = new_reproduction
        else:
            raise ValueError("Name must be filled")

    @property
    def food(self):
        return self._habitation

    @food.setter
    def food(self, new_food):
        if re.search(r'\S', new_food):
            self._food = new_food
        else:
            raise ValueError("Name must be filled")

    @property
    def shell_color(self):
        return self._shell_color

    @shell_color.setter
    def shell_color(self, new_color):
        if re.search(r'\S', new_color):
            self._shell_color = new_color
        else:
            raise ValueError("Color must be filled")

    def _i_am_reproducing(self):
        print(f'I am reproducing using {self._reproduction}')

    def _i_eat(self):
        print(f'I eat {self._food}')

    def _i_live(self):
        print(f'I live in {self._habitation}')

    def reproducing(self):
        self._i_am_reproducing()

    def eating(self):
        self._i_eat()

    def living(self):
        self._i_live()

    def _my_color(self):
        print(f'My shell color is {self._shell_color}')

    def color(self):
        self._my_color()


if __name__ == '__main__':
    crab = Crustacean('Eggs', 'Under Water', 'Everything', 'Red')
    crab.color()
    crab.living()
    crab.reproducing()
    crab.eating()
