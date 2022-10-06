class Company:
    def __init__(self, name_of_company: str, number_of_staff: int, products: list, country: str):
        self.__name_of_company = name_of_company
        self.__number_of_staff = number_of_staff
        self.__products = products
        self.__country = country

    @property
    def name_of_company(self):
        return self.__name_of_company

    @name_of_company.setter
    def company_name(self, new_title: str):
        """
            This function renames the company
        """
        self.__name_of_company = new_title

    @name_of_company.deleter
    def company_name(self):
        """
            This function does not allow users to delete name
        """
        pass

    @property
    def number_of_staff(self):
        return self.__number_of_staff

    def add_new_employees(self, number_of_new_employees: int):
        self.__number_of_staff = self.__number_of_staff + number_of_new_employees

    @number_of_staff.deleter
    def number_employees(self):
        """
            This function does not allow users to delete number of employees
        """
        pass

    @property
    def products(self):
        return self.__products

    def add_new_products(self, *args: tuple):
        """
           This function adds a new company's product
        """
        for arg in args:
            if arg not in self.__products:
                self.__products.append(arg)

    def out_of_stock(self, *args: tuple):
        """
            This function delete product that's out of stock
        """
        for arg in args:
            if arg in self.__products:
                self.__products.remove(arg)

    @products.deleter
    def products(self):
        """
            This function does not allow users to delete products
        """
        pass

    @property
    def country(self):
        """
            This function returns name of country
        """
        return self.__country

    @country.setter
    def country(self, relocate_to_another_country: str):
        """
            This function changes the name of the country
        """
        self.__country = relocate_to_another_country

    @country.deleter
    def country(self):
        """
            This function does not allow users to delete the name of the country
        """
        pass


if __name__ == '__main__':
    samsung = Company('Samsung Co.', 251987, ['Galaxy S22', 'Galaxy S22 Ultra', 'Samsung A73 5G'], 'Korea')
    print(samsung.products)
    samsung.add_new_products('Galaxy TAB', 'Samsung A55 KDSEK')
    samsung.out_of_stock('Samsung A73 5G')
    print(samsung.products)
