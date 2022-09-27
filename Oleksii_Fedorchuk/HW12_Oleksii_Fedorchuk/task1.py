class Company:
    """Class of the company description"""

    def __init__(self, company_name: str, company_website: str, company_description: str, company_products: str):
        """Initiation"""

        self.__company_name = company_name
        self.__company_website = company_website
        self.__company_description = company_description
        self.__company_products = company_products

    def company_name(self):
        """Show company name"""

        company_name = self.__company_name
        print(company_name)

    def company_products(self):
        """Show company products"""

        company_products = self.__company_products
        print(company_products)

    def company_website(self):
        """Show company website """

        company_website = self.__company_website
        print(company_website)

    def company_description(self):
        """Show company description"""

        description = (f"Company name is:{self.__company_name}\nCompany website is:{self.__company_website}\n"
                       f"Company description is:{self.__company_description}\n"
                       f"Company products are:{self.__company_products}")
        print(description)


if __name__ == "__main__":
    Apple = Company('Apple', "www.apple.com", "Hardware and Software developing", "Iphone")
    Apple.company_description()
    Google = Company('Google', "www.google.com", "Software developing", "Pixel")
    Google.company_name()
    Google.company_website()
    Google.company_products()

