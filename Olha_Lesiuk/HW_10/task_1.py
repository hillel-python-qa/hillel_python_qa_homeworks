class Company:

    # The init method or constructor
    def __init__(self, company_name: str, organisational_structure: dict, top_industries: list,
                 amount_of_employees: int):
        # Instance Variable
        self.__company_name = company_name
        self.__organisational_structure = organisational_structure
        self.__top_industries = top_industries
        self.__amount_of_employees = amount_of_employees

    @property
    def company_name(self):
        """
        The method is used to obtain worker's name
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name: str):
        """
        The method is used in case of changing the name of the company
        """
        if company_name:
            self.__company_name = company_name
        else:
            raise ValueError("The company name should not be empty!")

    @property
    def organisational_structure(self):
        """
        The method is used to obtain worker's name
        """
        return self.__organisational_structure

    @organisational_structure.setter
    def organisational_structure(self, organisational_structure: dict):
        """
        The method is used in case of changing the organisational structure of Toyota company
        """
        if organisational_structure:
            self.__organisational_structure = organisational_structure
        else:
            raise ValueError("The organizational structure should not be empty!")

    @property
    def top_industries(self):
        """
        The method is used to obtain top industries of the company
        """
        return self.__top_industries

    @top_industries.setter
    def top_industries(self, top_industries: list):
        """
        The method is used in case of changing of the top industries
        """
        if top_industries:
            self.__top_industries = top_industries
        else:
            raise ValueError("The top industries should not be empty!")

    @property
    def amount_of_employees(self):
        """
        The method is used to obtain general amount company's employees
        """
        return self.__amount_of_employees

    @amount_of_employees.setter
    def amount_of_employees(self, amount_of_employees: int):
        """
        The method is used in case of changing the amount of employees
        """
        if amount_of_employees > 0:
            self.__amount_of_employees = amount_of_employees
        else:
            raise ValueError("The amount of employees should be positive digit!")


if __name__ == '__main__':
    Company.organisational_structure = {'Toyota Motor Corp, (TMC)': 'Japan', 'Toyota Motor Credit Corp': 'Japan',
                                        'Toyota Motor Sales USA': 'Torrance, Calif',
                                        'Toyota Motor Engineering and Manufacturing': 'Erlanger, Ky',
                                        'Toyota Motor North America': 'New York', 'Toyota Financial Services': 'USA'}
    Company.industries = ['Materials Handling Equipment', 'Automobiles', 'Textile Machinery']

    print(Company.organisational_structure, Company.industries)
