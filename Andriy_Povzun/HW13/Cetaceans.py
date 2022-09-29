from Mammals import Mammals


class Cetaceans(Mammals):
    def __init__(self, kind_of_cetaceans):
        super().__init__('Cetaceans')
        self._kind_of_cetaceans = kind_of_cetaceans

    @property
    def kind_of_cetaceans(self):
        return self._kind_of_cetaceans

    def _i_eat(self):
        return f'{self._kind_of_mammal} feed on small crustaceans,fish, shellfish.'

    def what_eating(self):
        print(self._i_eat())

    def _my_special(self):
        return f'{self._kind_of_mammal} spend their whole lives in the water environment.' \
               f' {self._kind_of_mammal} have the largest representative of the genus {self.sub_group}, Blue whale'

    def uniqueness(self):
        """
        This method reflects the uniqueness of this species
        """
        print(self._my_special())

    def _i_live(self):
        return f'{self._kind_of_mammal} live in seas and oceans'

    def where_live(self):
        print(self._i_live())

    def __jump_out_of_the_water(self):
        return f'{self._kind_of_cetaceans} effectively jumped out of the water'

    def show_up(self):
        print(self.__jump_out_of_the_water())


if __name__ == '__main__':
    blue_whale = Cetaceans('Blue Whale')
    print(blue_whale.animal_group)
    print(blue_whale.sub_group)
    print(blue_whale.kind_of_mammal)
    print(blue_whale.kind_of_cetaceans)
    blue_whale.what_eating()
    blue_whale.uniqueness()
    blue_whale.where_live()
    blue_whale.show_up()
