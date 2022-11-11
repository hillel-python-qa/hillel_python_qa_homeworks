class Train:
    def __init__(self, number_of_wagons: list):
        self.__number_of_wagons = number_of_wagons

    @property
    def number_of_wagons(self):
        """
            Returns number of wagons
        """
        return self.__number_of_wagons

    @number_of_wagons.setter
    def number_of_wagons(self, value):
        """
            Takes one parameter, checks if it's larger than the largest number in the list by one, and appends it if
            the condition is true.
        """
        last = self.__number_of_wagons[-1]
        if type(value) == int and value == last + 1:
            self.__number_of_wagons.append(value)
        else:
            raise ValueError('Wagon number must be one greater than the last one')

    def __str__(self):
        """
            Replaces magic method __str__ with a loop that adds '-[n]' to the original string '<=[HEAD]' for each
            variable in number_of_wagons, where n is value of each variable in sorted list number_of_wagons.
        """
        locomotive = '<=[HEAD]'
        for wagon in sorted(self.__number_of_wagons):
            locomotive += f'-[{wagon}]'
        return locomotive


if __name__ == '__main__':
    list_of_wagons = [1, 2, 3, 4, 5, 6, 7, 8]
    Train_1 = Train(list_of_wagons)
    print(Train_1)
    Train_1.number_of_wagons = 9
    print(Train_1)
