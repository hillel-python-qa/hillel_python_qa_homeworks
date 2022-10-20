from animal_1 import Animal
import re


class Birds(Animal):
    def __init__(self, reproduction: str, habitation: str, food: str, wing_span: int):
        super().__init__(habitation, reproduction)
        self._food = food
        self._wing_span = wing_span

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
    def wing_span(self):
        """
            Returns wing_span value
        """
        return self._wing_span

    @wing_span.setter
    def wing_span(self, new_span):
        """
            Takes one parameter, check if it's int and more than zero and sets it's as new wing span
        """
        if type(new_span) is int and new_span > 0:
            self._wing_span = new_span
        else:
            raise ValueError("New span must be an int and more than 0")


if __name__ == '__main__':
    pigeon = Birds("Eggs", "City/Skies", "Seeds", 40)
    pigeon.reproducing()
    pigeon.living()
    pigeon.eating()