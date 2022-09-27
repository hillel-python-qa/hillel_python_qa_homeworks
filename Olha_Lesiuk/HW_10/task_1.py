class Toyota:
    # Class Variable
    company = 'Toyota'

    # The init method or constructor
    def __init__(self, organisational_structure: dict, top_industries: list):
        # Instance Variable
        self.__organisational_structure = organisational_structure
        self.__top_industries = top_industries

    @property
    def get_organisational_structure(self):
        return self.__organisational_structure

    def top_industries(self):
        return self.__top_industries


ToyotaOrgStructure = {'Toyota Motor Corp, (TMC)': 'Japan', 'Toyota Motor Credit Corp': 'Japan',
                      'Toyota Motor Sales USA': 'Torrance, Calif',
                      'Toyota Motor Engineering and Manufacturing': 'Erlanger, Ky',
                      'Toyota Motor North America': 'New York', 'Toyota Financial Services': 'USA'}

ToyotaTopIndustries = ['Materials Handling Equipment', 'Automobiles', 'Textile Machinery']

if __name__ == '__main__':
    print(Toyota.company)
    print(ToyotaOrgStructure)
    print(ToyotaTopIndustries)
