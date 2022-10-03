from Mammals import Mammals


class Rodents(Mammals):
    # This Class inherits kingdom, specie type, mammals_types arguments
    # from Mammals class (which can work for any animal)

    def __init__(self, kingdom: str, specie_type: str, mammals_types: str, rodents_types: str,
                 wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_type = mammals_types
        self.__rodents_types = rodents_types
        self.__wool_is_present = wool_is_present
        self.__name = name

    @property
    # this method is used to obtain the insectivorous type
    def rodents_types(self):
        return "The Rodents type is:", self.__rodents_types

    @rodents_types.setter
    # this method is used in case changing the rodents type
    def rodents_types(self, rodents_types):
        self.__rodents_types = rodents_types

    @property
    # this method is used to obtain that wool is present or not
    def wool_is_present(self):
        return "Is the wool present?", self.__wool_is_present

    @wool_is_present.setter
    # this method is used in case changing boolean value
    def wool_is_present(self, wool_is_present):
        self.__wool_is_present = wool_is_present

    @property
    # this method is used to determine a name of insectivorous
    def name(self):
        return "The name of the rodent is:", self.__name

    @name.setter
    # this method is used in case changing name of rodent
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    mouse = Rodents(kingdom="Animals", specie_type="Mammals",
                    mammals_types="Rodents", rodents_types="Mice", wool_is_present=True, name="Mouse")

    print(mouse.kingdom)
    print(mouse.specie_type)
    print(mouse.mammals_types)
    print(mouse.rodents_types)
    print(mouse.wool_is_present)
    print(mouse.name)
