from HannaPidchasiuk.HW11.mamals import Mammals


class FlyingMammals(Mammals):
    def __init__(self, species, number_of_subspecies, area_of_living, number_of_paws,
                 colour_of_feathers: str):
        super().__init__(species, number_of_subspecies, area_of_living, number_of_paws)
        self.__colour_of_feathers = colour_of_feathers

    @property
    def colour_of_feathers(self):
        """
            Returns colour of feathers of the flying mammal.
        """
        return self.__colour_of_feathers

    @colour_of_feathers.setter
    def colour_of_feathers(self, new_value):
        """
            Set new colour of feather of the flying mammal.
            Takes only 1 argument: new_value.
        """
        if new_value:
            self.__colour_of_feathers = new_value
        else:
            raise ValueError("colour_of_feathers can't be empty!")
