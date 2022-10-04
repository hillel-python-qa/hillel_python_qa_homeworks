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
