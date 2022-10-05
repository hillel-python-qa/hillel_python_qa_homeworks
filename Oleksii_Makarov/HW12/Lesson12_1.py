import re


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
        if re.search(r'\S', new_name):
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
        if type(new_value) == int and new_value >= 0:
            self.__employees = new_value
        else:
            raise TypeError("Number of employees must be a positive int")

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
        return self.__net_worth

    @net_worth.setter
    def net_worth(self, new_net_worth):
        """
            Set's net worth of company
            Checks if number is float
        """
        if type(new_net_worth) == float and new_net_worth >= 0:
            self.__net_worth = new_net_worth
        else:
            raise TypeError("Net worth must be a float above zero")

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
        # It seems that I can't compare it to true, else it would allow empty spaces
        if type(new_location) == str and re.search(r'\S', new_location):
            self.__hq_location = new_location
        else:
            raise TypeError("The location must be a string with words")

    @hq_location.deleter
    def hq_location(self):
        """
            Removes company's headquarters location. Boom.
        """
        self.__hq_location = None

    def taxes(self):
        """
            Pays 200$ per employee. Adjust networth afterwards.
        """
        overall_tax = (self.__employees * 200)
        after_taxes = self.__net_worth - overall_tax
        if after_taxes <= 0:
            print(f'You have too much employees! Your taxes are: {overall_tax}'
                  f'\nWhich is more than your networth:{self.__net_worth}')
        else:
            self.__net_worth = after_taxes
            print(f'Your taxes are: {overall_tax}'
                  f'\nNet worth after paying 200$ per employee: {self.__net_worth}$')

    def employees_change(self, change):
        """
            Function describing change of number of employees for a specific amount
        """
        if type(change) == int:
            if change < 0:
                if abs(change) > self.__employees:
                    raise ValueError("Number of employees cannot be less than zero")
                else:
                    self.__employees += change
            elif change == 0:
                raise ValueError("Change must not be a zero")
            else:
                self.__employees += change

        else:
            raise TypeError("Value must be an int")


if __name__ == '__main__':
    sony = Company("Sony", 109700, 80490000000, "Minato Coty, Tokyo, Japan")
    print(sony.name)
    print(sony.employees)
    print(sony.hq_location)
    print(sony.net_worth)
    sony.name = "Sony Corporation"
    print(sony.name)
    sony.employees_change(-1000)
    print(sony.employees)
    sony.hq_location = "A A"
    print(sony.hq_location)
    sony.name = "A"
    sony.taxes()
