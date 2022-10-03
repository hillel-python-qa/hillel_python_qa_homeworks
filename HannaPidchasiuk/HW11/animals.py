from HannaPidchasiuk.HW11.area_of_living_enum import AreaOfLiving


class Animals:
    def __init__(self, species: str, number_of_subspecies: int, area_of_living: AreaOfLiving):
        self.__species = species
        self.__number_of_subspecies = number_of_subspecies
        self.__area_of_living = area_of_living

    @property
    def species(self):
        """
            Returns name of the species.
        """
        return self.__species

    @species.setter
    def species(self, new_value: str):
        """
            Set new species of the animal.
            Takes only 1 argument: new_value.
        """
        if new_value:
            self.__species = new_value
        else:
            raise ValueError("species can't be empty!")

    @property
    def number_of_subspecies(self):
        """
            Returns number of subspecies.
        """
        return self.__number_of_subspecies

    @number_of_subspecies.setter
    def number_of_subspecies(self, new_value: int):
        """
            Set new number of subspecies of the animal.
            Takes only 1 argument: new_value.
        """
        if not new_value < 0:
            self.__number_of_subspecies = new_value
        else:
            raise ValueError("number_of_subspecies can't be less than zero!")

    @property
    def area_of_living(self):
        """
            Returns area of living of the animal.
        """
        return self.__area_of_living

    @area_of_living.setter
    def area_of_living(self, new_value: AreaOfLiving):
        """
            Set new area of living of the animal.
            Takes only 1 argument: new_value.
        """
        self.__area_of_living = new_value

    def subspecies_die(self):
        """
            Decreases number of subspecies.
        """
        if self.__number_of_subspecies >= 1:
            return self.__number_of_subspecies - 1
        else:
            print("All subspecies already dead.")

    def found_new_subspecies(self):
        """
            Increases number of the subspecies.
        """
        return self.__number_of_subspecies + 1
