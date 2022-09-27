class Company:
    """
    Class Company that contain name, industry, employees, headquarter, product and services.
    """

    def __init__(self, name: str, industry: str, employees: list, headquarter: str, product: set, service: set):
        self.__name = name
        self.__industry = industry
        self.__employees = employees
        self.__headquarter = headquarter
        self.__product = product
        self.__service = service

    @property
    def name(self):
        """
        A method to get the company's name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        A method to change the company's name
        """
        self.__name = new_name

    @property
    def industry(self):
        """
        A method to get the company's industry
        """
        return self.__industry

    @industry.setter
    def industry(self, new_industry: str):
        """
        A method to update the company's industry
        """
        self.__industry = new_industry

    @property
    def employees(self):
        """
        A method to get the company's number of employees
        """
        return self.__employees

    @employees.setter
    def employees(self, new_employees_number: int):
        """
        A method to update company's employees number
        """
        if new_employees_number > -1:
            self.__employees = new_employees_number
        else:
            raise ValueError("The number of employees can not be negative")

    def add_employee(self, new_employee_number=1):
        """
        A method to add the number of employees to the existing one
        """
        return sum(self.__employees, new_employee_number)

    @property
    def headquarter(self):
        """
        A method to get the headquarters
        """
        return self.__headquarter

    @headquarter.setter
    def headquarter(self, new_headquarter: str):
        # if new_headquarter != "":
        self.__headquarter = new_headquarter
        # else:
        #     raise ValueError("Headquarters name can not be empty")

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, new_product: str):
        if new_product in self.__product:
            raise ValueError(f"{new_product} can not be added")
        else:
            self.__product.add(new_product)

    def remove_product(self, product_to_remove: str):
        if product_to_remove in self.__product:
            self.__product.remove(product_to_remove)
        else:
            raise ValueError(f"{product_to_remove} can not be removed")

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, new_service):
        if new_service in self.__service:
            raise ValueError(f"{new_service} can not be added")
        else:
            self.__service.add(new_service)

    def remove_service(self, service_to_remove: str):
        if service_to_remove in self.__service:
            self.__service.remove(service_to_remove)
        else:
            raise ValueError(f"{service_to_remove} can not be removed")
