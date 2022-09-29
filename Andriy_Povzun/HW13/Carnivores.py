from Mammals import Mammals
import random


class Carnivores(Mammals):
    def __init__(self, kind_of_carnivores):
        super().__init__('Carnivores')
        self._kind_of_carnivores = kind_of_carnivores

    @property
    def kind_of_carnivores(self):
        return self._kind_of_carnivores

    def _i_eat(self):
        return f'{self.kind_of_mammal} mainly feed on other animals'

    def what_eating(self):
        print(self._i_eat())

    def _my_special(self):
        return f'{self.kind_of_mammal} by nature, they are endowed with very sensitive ' \
               f'hearing and smell, and they see well at night'

    def uniqueness(self):
        """
        This method reflects the uniqueness of this species
        """
        print(self._my_special())

    def _i_live(self):
        return f'{self.kind_of_mammal} inhabit all the continents of our planet'

    def where_live(self):
        print(self._i_live())

    def __catch_prey(self):
        preys = ('Fish', 'Rabbit', 'Deer', 'Fallow Deer', 'Antelope')
        return f'{self._kind_of_carnivores} catch {random.choice(preys)}'

    def go_hunt(self):
        print(self.__catch_prey())


if __name__ == '__main__':
    wolf = Carnivores('Wolf')
    print(wolf.animal_group)
    print(wolf.sub_group)
    print(wolf.kind_of_mammal)
    print(wolf.kind_of_carnivores)
    wolf.what_eating()
    wolf.uniqueness()
    wolf.where_live()
    wolf.go_hunt()
