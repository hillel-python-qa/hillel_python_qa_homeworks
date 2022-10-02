class Apple:

    def __init__(self, name: str, employees: list, products: list, shops: list):
        self.__name = name
        self.__employees = employees
        self.__products = products
        self.__shops = shops

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Name cannot be empty
        """
        if name == '':
            raise Exception('No empty name!')
        else:
            self.__name = name

    @property
    def employees(self) -> list:
        return self.__employees

    @property
    def products(self) -> list:
        return self.__products

    @property
    def shops(self):
        return self.__shops

    def add_employee(self, employee):
        self.__employees().append(employee)

    def remove_employee(self, employee):
        self.__employees().remove(employee)

    def add_product(self, product):
        self.__products().append(product)

    def remove_product(self, product):
        self.__products().remove(product)

    def add_shop(self, shop):
        self.__shops().append(shop)

    def remove_shop(self, shop):
        self.__shops().remove(shop)

    def get_employees_count(self) -> int:
        return len(self.__employees)
