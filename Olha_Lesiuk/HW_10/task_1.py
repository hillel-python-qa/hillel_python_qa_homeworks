class Company:

    # The init method or constructor
    def __init__(self, company_name: str, organisational_structure: dict, top_industries: list):
        # Instance Variable
        self.__company_name = company_name
        self.__organisational_structure = organisational_structure
        self.__top_industries = top_industries

    @property
    def company_name(self):
        return self.__company_name

    @property
    def get_organisational_structure(self):
        return self.__organisational_structure

    @property
    def top_industries(self):
        return self.__top_industries


if __name__ == '__main__':
    Company.organisational_structure = {'Toyota Motor Corp, (TMC)': 'Japan', 'Toyota Motor Credit Corp': 'Japan',
                                        'Toyota Motor Sales USA': 'Torrance, Calif',
                                        'Toyota Motor Engineering and Manufacturing': 'Erlanger, Ky',
                                        'Toyota Motor North America': 'New York', 'Toyota Financial Services': 'USA'}
    Company.industries = ['Materials Handling Equipment', 'Automobiles', 'Textile Machinery']

    print(Company.organisational_structure, Company.industries)
