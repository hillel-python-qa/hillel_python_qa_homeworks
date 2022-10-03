from hillel_python_qa_homeworks.Andriy_Povzun.HW13.Carnivores import Carnivores


# Inheritance
class Wolfs(Carnivores):
    def __init__(self, kind_of_wolf: str):
        super().__init__('Wolf')
        # Hiding
        self._kind_of_wolf = kind_of_wolf

    # encapsulation
    @property
    def kind_of_wolf(self):
        return self._kind_of_wolf

    # Hiding
    # Polymorphism
    # encapsulation
    def _i_eat(self):
        return f'{self._kind_of_carnivores} eat goats, sheep, deer, elk, wild boar, roe deer'

    # Hiding
    # Polymorphism
    # encapsulation
    def _my_special(self):
        return f'{self._kind_of_carnivores} a very dangerous animal that usually hunts in packs, ' \
               f'and poses a threat to humans in the wild'

    # Hiding
    # Polymorphism
    # encapsulation
    def _i_live(self):
        return f'The {self._kind_of_carnivores} is distributed quite widely - ' \
               f'it occurs in Europe, Asia and North America'


if __name__ == '__main__':
    wolf = Wolfs('Arctic Wolf')
    print(wolf.animal_group)
    print(wolf.sub_group)
    print(wolf.kind_of_mammal)
    print(wolf.kind_of_carnivores)
    print(wolf.kind_of_wolf)
    wolf.what_eating()
    wolf.uniqueness()
    wolf.where_live()
    wolf.go_hunt()
