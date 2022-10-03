from HannaPidchasiuk.HW11.area_of_living_enum import AreaOfLiving
from HannaPidchasiuk.HW11.mamals import Mammals


class Predators(Mammals):

    def __init__(self, species, number_of_subspecies, area_of_living, number_of_paws,
                 number_of_teeth: int):
        super().__init__(species, number_of_subspecies, area_of_living, number_of_paws)
        self.__number_of_teeth = number_of_teeth

    @property
    def number_of_teeth(self):
        """
            Returns number of teeth of the predator.
        """
        return self.__number_of_teeth

    @number_of_teeth.setter
    def number_of_teeth(self, new_value: int):
        """
            Set new number of teeth of the predator.
            Takes only 1 argument: new_value.
        """
        if not new_value < 0:
            self.__number_of_teeth = new_value
        else:
            raise ValueError("number_of_teeth can't be less than zero!")

    def lose_tooth(self):
        """
            Decreases nuber of teeth.
        """
        if self.__number_of_teeth > 0:
            return self.__number_of_teeth - 1
        else:
            print("No tooth to lose.")


if __name__ == '__main__':
    cat = Predators("Cat", 40, AreaOfLiving.SAVANNA, 4, 40)
    cat.subspecies_die()
    cat.found_new_subspecies()
    cat.lose_tooth()
