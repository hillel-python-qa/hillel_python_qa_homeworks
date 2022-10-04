class Company:
    def __init__(self, name: str, employees: int, net_worth: float, hq_location: str):
        self.__name = name
        self.__employees = employees
        self.__net_worth = net_worth
        self.__hq_location = hq_location

    @property
    def name(self):
        """
            Returns company's name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
            Sets new name for company if it's not an empty space
        """
        if new_name:
            self.__name = new_name
        else:
            raise ValueError("Name must be filled")

    @property
    def employees(self):
        """
            Returns the number of employees
        """
        return self.__employees

    @employees.setter
    def employees(self, new_value):
        """
            Replaces the number of employees
        """
        if type(new_value) == int:
            self.__employees = new_value
        else:
            raise TypeError("Number of employees must be an int")

    def employees_plus(self, additional):
        """
            Function describing addition of number of employees
        """
        if type(additional) == int:
            self.__employees += additional
        else:
            raise TypeError("Value must be int")

    @employees.deleter
    def employees(self):
        """
            Sets the number of employees to None
        """
        self.__employees = None

    @property
    def net_worth(self):
        """
            Returns company's net worth in USD
        """
        return f'{self.__net_worth}$'

    @net_worth.setter
    def net_worth(self, new_net_worth):
        """
            Set's net worth of company
            Checks if number is float
        """
        if type(new_net_worth) == float:
            self.__net_worth = new_net_worth
        else:
            raise TypeError("Net worth must be float")

    @net_worth.deleter
    def net_worth(self):
        """
            Removes company's net worth.
        """
        # Maybe I should set it to zero?
        self.__net_worth = None

    @property
    def hq_location(self):
        """
            Returns the location of company's Headquarters
        """
        return self.__hq_location

    @hq_location.setter
    def hq_location(self, new_location):
        """
            Set a new location for a company's HQ if it's string
        """
        if type(new_location) == str:
            self.__hq_location = new_location
        else:
            raise TypeError("The location must be a string")

    @hq_location.deleter
    def hq_location(self):
        """
            Removes company's headquarters location. Boom.
        """
        self.__hq_location = None


if __name__ == '__main__':
    sony = Company("Sony", 109700, 80490000000, "Minato Coty, Tokyo, Japan")
    print(sony.name)
    print(sony.employees)
    print(sony.hq_location)
    print(sony.net_worth)
    sony.name = "Sony Corporation"
    print(sony.name)
    sony.employees_plus(800)
    print(sony.employees)
