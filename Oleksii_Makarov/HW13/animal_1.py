import re
from abc import ABC,abstractmethod


class Animal(ABC):
    def __init__(self, species: str, habitation: str, size: str):
        self.__species = species
        self.__habitation = habitation
        self.__size = size

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species_name):
        if re.search(r'\S', species_name):
            self.__species = species_name
        else:
            raise NameError("Species name should be filled")

    @property
    def habitation(self):
        return self.__habitation

    @habitation.setter
    def habitation(self, habitation_name):
        if re.search(r'\S', habitation_name):
            self.__species = habitation_name
        else:
            raise NameError("Habitation name should be filled")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size_value):
        if re.search(r'\S', size_value):
            self.__size = size_value
        else:
            raise NameError("Size value  be filled")

    @abstractmethod
    def _i_eat(self):
        pass

    @abstractmethod
    def _i_am_threatened(self):
        pass