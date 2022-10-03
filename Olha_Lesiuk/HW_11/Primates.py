from Mammals import Mammals


class Primates(Mammals):
    # This Class inherits kingdom, specie type, mammals_types arguments
    # from Mammals class (which can work for any animal)

    def __init__(self, kingdom: str, specie_type: str, mammals_types: str, primates_types: str,
                 wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_type = mammals_types
        self.__primates_types = primates_types
        self.__wool_is_present = wool_is_present
        self.__name = name

    @property
    # this method is used to obtain the primates type
    def primates_types(self):
        return "The Primates type is:", self.__primates_types

    @primates_types.setter
    # this method is used in case changing the primates type
    def primates_types(self, primates_types):
        self.__primates_types = primates_types

    @property
    # this method is used to obtain that wool is present or not
    def wool_is_present(self):
        return "Is the wool present?", self.__wool_is_present

    @wool_is_present.setter
    # this method is used in case changing boolean value
    def wool_is_present(self, wool_is_present):
        self.__wool_is_present = wool_is_present

    @property
    # this method is used to determine a name of primates
    def name(self):
        return "The name of the primates is:", self.__name

    @name.setter
    # this method is used in case changing name of primates
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    lemur = Primates(kingdom="Animals", specie_type="Mammals",
                     mammals_types="Primates", primates_types="Lemurs", wool_is_present=True, name="Lemur catta")

    print(lemur.kingdom)
    print(lemur.specie_type)
    print(lemur.mammals_types)
    print(lemur.primates_types)
    print(lemur.wool_is_present)
    print(lemur.name)
