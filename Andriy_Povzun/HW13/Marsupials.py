from Mammals import Mammals


class Marsupials(Mammals):
    def __init__(self, kind_of_marsupial: str):
        super().__init__('Marsupials')
        self._kind_of_marsupial = kind_of_marsupial

    @property
    def kind_of_marsupial(self):
        return self._kind_of_marsupial

    def _i_eat(self):
        return f'{self._kind_of_mammal} eat grass, insects and etc...'

    def what_eating(self):
        print(self._i_eat())

    def _my_special(self):
        return f'{self._kind_of_mammal} bear children inside for only a few weeks, ' \
               'then the bearing continues in the outer bag'

    def uniqueness(self):
        """
        This method reflects the uniqueness of this species
        """
        print(self._my_special())

    def _i_live(self):
        return f'{self._kind_of_mammal} live in Australia, USA'

    def where_live(self):
        print(self._i_live())

    def __jumping(self):
        return f'{self._kind_of_marsupial} jumping'

    def jump(self):
        print(self.__jumping())


if __name__ == '__main__':
    just_test = Marsupials('Kangaroo')
    just_test.uniqueness()
    just_test.where_live()
    just_test.what_eating()
    just_test.jump()
    print(just_test.kind_of_marsupial)
    print(just_test.animal_group)
    print(just_test.kind_of_mammal)
    print(just_test.sub_group)
