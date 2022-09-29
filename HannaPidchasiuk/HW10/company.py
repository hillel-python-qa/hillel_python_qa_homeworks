import re


class Company:

    def __init__(self, name: str, number_of_employees: int, products: list[str], website: str):
        self.__name = name
        self.__number_of_employees = number_of_employees
        self.__products = products
        self.__website = website

    @property
    def name(self):
        """
            Returns name of the company.
        """
        return self.__name

    @name.setter
    def name(self, new_value: str):
        """
            Set new name of the worker.
            Takes only 1 argument: new_value.
        """
        if new_value:
            self.__name = new_value
        else:
            raise ValueError("New value can't be empty!")

    @property
    def number_of_employees(self):
        """
            Returns number of employees of the company.
        """
        return self.__number_of_employees

    @number_of_employees.setter
    def number_of_employees(self, new_value: int):
        """
            Set new number_of_employees of the company.
            Takes only 1 argument: new_value.
        """
        if new_value < 0:
            raise ValueError("Number of employees can't be less than 0!")
        else:
            self.__number_of_employees = new_value

    @property
    def products(self) -> list[str]:
        """
            Returns list of products of the company.
        """
        return self.__products

    @products.setter
    def products(self, new_value: str):
        """
            Add new product to products.
            Takes only 1 argument: new_value.
        """
        if new_value in self.__products:
            raise ValueError("Product already exists!")
        else:
            self.__products.append(new_value)

    @property
    def website(self):
        """
            Returns web_site of the company.
        """
        return self.__website

    @website.setter
    def website(self, new_value: str):
        """
            Set new website of the company.
            Takes only 1 argument: new_value.
        """
        if re.match(r'^(?:http:\/\/|www\.|https:\/\/)([^\/]+)', new_value):
            self.__website = new_value
        else:
            raise ValueError("Incorrect website provided!")

    def add_many_products(self, *args: str):
        """
            Adds many products to the list if they are not exists.
        """
        self.__products = list(set(self.__products).union(set(args)))

    def remove_one_product(self, product_to_remove: str):
        """
            Check if product is in list and removes it from the products list.
        """
        if product_to_remove in self.__products:
            self.__products.remove(product_to_remove)
        else:
            print(f"No '{product_to_remove}' product to remove.")

    def remove_many_products(self, *args: str):
        """
            Removes many products from the list if they are exists.
        """
        for product in args:
            self.remove_one_product(product)

    def get_domain_from_website(self):
        """
            Returns domain name from website.
        """
        website_pattern = re.compile(r'^(?:http:\/\/|www\.|https:\/\/)([^\/]+)')
        domain = re.findall(website_pattern, self.__website)
        if domain is not None:
            return domain
        else:
            raise ValueError("Incorrect website provided!")


if __name__ == "__main__":
    company = Company("Test", 1000, ["1", "2", "test"], "https://www.w3schools.com/python/python_regex.asp")
    # company.website = "skjdfdkjf"
    company.remove_many_products("2", "0")
    company.add_many_products("1", "3")
    print(company.products)
    print(company.get_domain_from_website())
