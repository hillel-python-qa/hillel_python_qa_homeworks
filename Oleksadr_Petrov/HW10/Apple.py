class Apple:

    def __init__(self, name: str, employees: list, products: list, customers: list):
        self.name = name
        self.employees = employees
        self.products = products
        self.customers = customers

    @property
    def employees(self):
        return self.employees

    @property
    def products(self):
        return self.products

    @property
    def employees(self):
        return self.customers

    def add_employee(self, employee):
        self.employees().append(employee)

    def remove_employee(self, employee):
        self.employees().remove(employee)

    def add_product(self, product):
        self.products().append(product)

    def remove_product(self, product):
        self.products().remove(product)

    def add_customer(self, customer):
        self.customers().append(customer)

    def remove_customer(self, customer):
        self.customers().remove(customer)





