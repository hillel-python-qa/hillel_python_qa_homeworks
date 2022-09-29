from Mammals import Mammals


class Primates(Mammals):
    def __init__(self, kind_of_primates: str):
        super().__init__('Primates')
        self._kind_of_primates = kind_of_primates

    @property
    def kind_of_primates(self):
        return self._kind_of_primates

    def _i_eat(self):
        return f'{self._kind_of_mammal} eat leaves, tree gum, fruits and plant contents, ' \
               f'insects and even more complex animal food.'

    def what_eating(self):
        print(self._i_eat())

    def _my_special(self):
        return f'{self._kind_of_mammal} unique in that they are intellectually very capable, most similar to humans.'

    def uniqueness(self):
        """
        This method reflects the uniqueness of this species
        """
        print(self._my_special())

    def _i_live(self):
        return f'{self._kind_of_mammal} common in tropical and subtropical regions' \
               f' of North and South America, Africa and Asia.'

    def where_live(self):
        print(self._i_live())

    def __jump_on_trees(self):
        return f'{self._kind_of_primates} jumping on trees'

    def have_fun(self):
        print(self.__jump_on_trees())


if __name__ == '__main__':
    chimpanzee = Primates('Chimpanzee')
    print(chimpanzee.animal_group)
    print(chimpanzee.sub_group)
    print(chimpanzee.kind_of_mammal)
    print(chimpanzee.kind_of_primates)
    chimpanzee.what_eating()
    chimpanzee.uniqueness()
    chimpanzee.where_live()
    chimpanzee.have_fun()
