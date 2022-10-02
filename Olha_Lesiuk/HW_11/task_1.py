# creating a parent class

class Animals:

    # initialization function
    # initialization the animal name,and specie type

    def __init__(self, kingdom: str, specie_type: str):
        self.__kingdom = kingdom
        self. __specie_type = specie_type

    # this method is used to obtain the kingdom name, it shouldn't change because we know that it is Animals

    @property
    def kingdom(self):
        return "The name of the kingdom is:", self.__kingdom

    # this method is used to obtain the specie type, it shouldn't change because we know that it is Mammals

    @property
    def specie_type(self):
        return "The specie type is:", self.__specie_type

        # creating the Mammals class as child class of Animal kingdom


class Mammals(Animals):
    # This Class inherits kingdom and specie type arguments from Animal class (which can work for any animal)
    def __init__(self, kingdom: str, specie_type: str, mammals_types: str):
        super().__init__(kingdom, specie_type)
        self.__mammals_types = mammals_types

    @property
    # this method is used to obtain the mammals type
    def mammals_types(self):
        return "The mammals type is:", self.__mammals_types

    @mammals_types.setter
    # this method is used in case of mammals types changing
    def mammals_types(self, mammals_types):
        self.__mammals_types = mammals_types


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
    test = Rodents(kingdom="Animals", specie_type="Mammals", mammals_types="Rodents", rodents_types="Mouse",
                   wool_is_present=False, name="Mouse")

    print(test.kingdom, test.specie_type, test.mammals_types, test.rodents_types, test.wool_is_present, test.name)
