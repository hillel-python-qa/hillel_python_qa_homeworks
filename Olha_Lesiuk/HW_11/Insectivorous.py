from hillel_python_qa_homeworks.Olha_Lesiuk.HW_11.Mammals import Mammals


class Insectivorous(Mammals):
    # This Class inherits kingdom, specie type, mammals_types arguments
    # from Mammals class (which can work for any animal)

    def __init__(self, kingdom: str, specie_type: str, mammals_types: str, insectivorous_types: str,
                 wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_type = mammals_types
        self.__insectivorous_types = insectivorous_types
        self.__wool_is_present = wool_is_present
        self.__name = name

    @property
    # this method is used to obtain the insectivorous type
    def insectivorous_types(self):
        return "The Insectivorous type is:", self.__insectivorous_types

    @insectivorous_types.setter
    # this method is used in case changing the insectivorous type
    def insectivorous_types(self, insectivorous_types):
        self.__insectivorous_types = insectivorous_types

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
        return "The name of the insectivorous is:", self.__name

    @name.setter
    # this method is used in case changing name of insectivorous
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    gecko = Insectivorous(kingdom="Animals", specie_type="Mammals",
                          mammals_types="Insectivorous", insectivorous_types="Lizards",
                          wool_is_present=False, name="Australian Gecko")

    print(gecko.kingdom)
    print(gecko.specie_type)
    print(gecko.mammals_types)
    print(gecko.insectivorous_types)
    print(gecko.wool_is_present)
    print(gecko.name)
