from HannaPidchasiuk.HW11.animals import Animals


class Mammals(Animals):

    def __init__(self, species, number_of_subspecies, area_of_living, number_of_paws: int):
        super().__init__(species, number_of_subspecies, area_of_living)
        self.__number_of_paws = number_of_paws

    @property
    def number_of_paws(self):
        """
            Returns number of paws of the mammal.
        """
        return self.__number_of_paws

    @number_of_paws.setter
    def number_of_paws(self, new_value):
        """
            Set new number of paws of the mammal.
            Takes only 1 argument: new_value.
        """
        if not new_value < 0:
            self.__number_of_paws = new_value
        else:
            raise ValueError("number_of_paws can't be less than zero!")

    def should_create_children(self):
        """
            If number of subspecies is low - need to create children.
        """
        if self.number_of_subspecies < 10:
            return True
        else:
            return False
