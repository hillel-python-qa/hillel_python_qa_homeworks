from Animal import Animal


class Mammals(Animal):
    def __init__(self, kind_of_mammal: str):
        super().__init__('Vertebrate', 'Mammals')
        self._kind_of_mammal = kind_of_mammal

    @property
    def kind_of_mammal(self):
        return self._kind_of_mammal

    def _i_eat(self):
        return f'{self._sub_group} eat a lot of everything'

    def what_eating(self):
        print(self._i_eat())

    def _my_special(self):
        return f'{self._sub_group} only have place for internal fertilization.' \
               f'The only {self._sub_group} animal that has mammary glands'

    def uniqueness(self):
        """
        This method reflects the uniqueness of this species
        """
        print(self._my_special())

    def _i_live(self):
        return f'{self._sub_group} live all over the world'

    def where_live(self):
        print(self._i_live())
