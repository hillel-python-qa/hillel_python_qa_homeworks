from HannaPidchasiuk.HW11.area_of_living_enum import AreaOfLiving


class Animals:
    def __init__(self, species: str, subspecies: str, number_of_subspecies: int, area_of_living: AreaOfLiving):
        self.__species = species
        self.__subspecies = subspecies
        self.__number_of_subspecies = number_of_subspecies
        self.__area_of_living = area_of_living

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, new_value: str):
        if new_value:
            self.__species = new_value
        else:
            raise ValueError("New value can't be empty!")

    @property
    def subspecies(self):
        return self.__subspecies

    @subspecies.setter
    def subspecies(self, new_value: str):
        if new_value:
            self.__subspecies = new_value
        else:
            raise ValueError("New value can't be empty!")

    @property
    def number_of_subspecies(self):
        return self.__number_of_subspecies

    @number_of_subspecies.setter
    def number_of_subspecies(self, new_value: int):
        if not new_value < 0:
            self.__number_of_subspecies = new_value
        else:
            raise ValueError("New value can't be less than zero!")

    @property
    def area_of_living(self):
        return self.__area_of_living

    @area_of_living.setter
    def area_of_living(self, new_value: AreaOfLiving):
        self.__area_of_living = new_value
