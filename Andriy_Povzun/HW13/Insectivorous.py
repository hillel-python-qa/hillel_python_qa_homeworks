from Mammals import Mammals


class Insectivorous(Mammals):
    def __init__(self, kind_of_insectivorous: str):
        super().__init__('Insectivorous')
        self._kind_of_insectivorous = kind_of_insectivorous

    @property
    def kind_of_insectivorous(self):
        return self._kind_of_insectivorous

    def _i_eat(self):
        return f'{self._kind_of_mammal} eating insects, worms, snails'

    def what_eating(self):
        print(self._i_eat())

    def _my_special(self):
        return f'The overwhelming number {self._kind_of_mammal.lower()} live in ground.' \
               ' The nose is elongated in the form of a proboscis.'

    def uniqueness(self):
        """
        This method reflects the uniqueness of this species
        """
        print(self._my_special())

    def _i_live(self):
        return f'{self._kind_of_mammal} live in Africa, Eurasia, Australia, Cuba'

    def where_live(self):
        print(self._i_live())

    def __saw_danger(self):
        return f'{self._kind_of_insectivorous} fled into the hole'

    def hide_from_predator(self):
        print(self.__saw_danger())


if __name__ == '__main__':
    hedgehog = Insectivorous('Hedgehog')
    print(hedgehog.animal_group)
    print(hedgehog.sub_group)
    print(hedgehog.kind_of_mammal)
    print(hedgehog.kind_of_insectivorous)
    hedgehog.what_eating()
    hedgehog.uniqueness()
    hedgehog.where_live()
    hedgehog.hide_from_predator()
