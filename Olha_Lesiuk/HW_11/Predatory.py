from hillel_python_qa_homeworks.Olha_Lesiuk.HW_11.Mammals import Mammals


class Predatory(Mammals):
    # This Class inherits kingdom, specie type, mammals_types arguments
    # from Mammals class (which can work for any animal)

    def __init__(self, kingdom: str, specie_type: str, mammals_types: str, predatory_types: str,
                 wool_is_present: bool, name: str):
        super().__init__(kingdom, specie_type, mammals_types)
        self.__kingdom = kingdom
        self.__specie_type = specie_type
        self.__mammals_type = mammals_types
        self.__predatory_types = predatory_types
        self.__wool_is_present = wool_is_present
        self.__name = name

    @property
    # this method is used to obtain the predatory type
    def predatory_types(self):
        return "The Predatory type is:", self.__predatory_types

    @predatory_types.setter
    # this method is used in case changing the predatory type
    def predatory_types(self, predatory_types):
        self.__predatory_types = predatory_types

    @property
    # this method is used to obtain that wool is present or not
    def wool_is_present(self):
        return "Is the wool present?", self.__wool_is_present

    @wool_is_present.setter
    # this method is used in case changing boolean value
    def wool_is_present(self, wool_is_present):
        self.__wool_is_present = wool_is_present

    @property
    # this method is used to determine a name of predatory
    def name(self):
        return "The name of the predatory is:", self.__name

    @name.setter
    # this method is used in case changing name of predatory
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    lion = Predatory(kingdom="Animals", specie_type="Mammals",
                     mammals_types="Predatory", predatory_types="Carnivore", wool_is_present=True, name="Lion")

    print(lion.kingdom)
    print(lion.specie_type)
    print(lion.mammals_types)
    print(lion.predatory_types)
    print(lion.wool_is_present)
    print(lion.name)
