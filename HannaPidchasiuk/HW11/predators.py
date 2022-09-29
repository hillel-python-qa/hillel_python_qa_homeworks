from HannaPidchasiuk.HW11.mamals import Mammals


class Predators(Mammals):

    def __init__(self, species, number_of_subspecies, area_of_living, number_of_paws,
                 number_of_teeth: int):
        super().__init__(species, number_of_subspecies, area_of_living, number_of_paws)
        self.__number_of_teeth = number_of_teeth

    @property
    def number_of_teeth(self):
        return self.__number_of_teeth

    @number_of_teeth.setter
    def number_of_teeth(self, new_value: int):
        if not new_value < 0:
            self.__number_of_teeth = new_value
        else:
            raise ValueError("number_of_teeth can't be less than zero!")

