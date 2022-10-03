from Animals import Animals


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
