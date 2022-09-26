class Company:
    def __init__(self, company_name: str, number_employees: int, company_products: list, country: str):
        self.__company_name = company_name
        self.__number_employees = number_employees
        self.__company_products = company_products
        self.__country = country

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, new_company_name: str):
        self.__company_name = new_company_name

    """
    The method is used to change the company name
    """

    @company_name.deleter
    def company_name(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def number_employees(self):
        return self.__number_employees

    def add_new_employees(self, quantity_new_employees: int):
        self.__number_employees = self.__number_employees + quantity_new_employees

    @number_employees.deleter
    def number_employees(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def company_products(self):
        return self.__company_products

    def add_new_products(self, *args: str):
        self.__company_products.append(*args)

    """
    The method is used to add new company products
    """

    def withdraw_from_production(self, *args: str):
        for arg in args:
            if arg not in self.__company_products:
                raise TypeError(f'Тo such element exists: {arg}')
            else:
                self.__company_products.remove(arg)

    """
    The method is used to withdraw products remove the product/products from production
    """

    @company_products.deleter
    def company_products(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country: str):
        self.__country = new_country

    @country.deleter
    def country(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """


if __name__ == '__main__':
    apple = Company('Apple inc.', 80000, ['MacBook', 'iPhone', 'AirPods'], 'USA')
    print(apple.company_products)
    apple.add_new_products('iPad, iPod')
    print(apple.company_products)
    apple.withdraw_from_production('MacBook', 'iPhone')
    print(apple.company_products)
