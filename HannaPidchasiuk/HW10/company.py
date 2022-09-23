class Company:

    def __init__(self, name: str, number_of_employees: int, products: list[str]):
        self.__name = name
        self.__number_of_employees = number_of_employees
        self.__products = products

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def number_of_employees(self):
        return self.__number_of_employees

    @number_of_employees.setter
    def number_of_employees(self, value: int):
        self.__number_of_employees = value

    @property
    def products(self) -> list[str]:
        return self.__products

    @products.setter
    def products(self, value: str):
        self.__products.append(value)
