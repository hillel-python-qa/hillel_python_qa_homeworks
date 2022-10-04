from Mammals import Mammals


class EvenToed(Mammals):
    # This Class inherits kingdom, specie type, mammals_types arguments
    # from Mammals class (which can work for any animal)

    def __init__(self, kingdom: str, specie_type: str, mammals_types: str, even_toed_types: str,
                 wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_type = mammals_types
        self.__even_toed_types = even_toed_types
        self.__wool_is_present = wool_is_present
        self.__name = name

    @property
    # this method is used to obtain the even-toed type
    def even_toed_types(self):
        return "The Even-toed type is:", self.__even_toed_types

    @even_toed_types.setter
    # this method is used in case changing the even-toed type
    def even_toed_types(self, even_toed_types):
        self.__even_toed_types = even_toed_types

    @property
    # this method is used to obtain that wool is present or not
    def wool_is_present(self):
        return "Is the wool present?", self.__wool_is_present

    @wool_is_present.setter
    # this method is used in case changing boolean value
    def wool_is_present(self, wool_is_present):
        self.__wool_is_present = wool_is_present

    @property
    # this method is used to determine a name of even-toed
    def name(self):
        return "The name of the even-toed is:", self.__name

    @name.setter
    # this method is used in case changing name of even-toed
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    pig = EvenToed(kingdom="Animals", specie_type="Mammals",
                   mammals_types="Even-Toed", even_toed_types="Pigs", wool_is_present=False, name="Yorkshire pig")

    print(pig.kingdom)
    print(pig.specie_type)
    print(pig.mammals_types)
    print(pig.even_toed_types)
    print(pig.wool_is_present)
    print(pig.name)
