class Sony:
    def __init__(self, department: str, location: str, company_name='Sony'):
        self.__department = department
        self.__location = location
        self.__company_name = company_name

        if self.__company_name != ('Sony' or 'sony'):
            raise TypeError('Only "Sony" company name available')

    @property
    def get_department(self):
        """
        Return department name
        """
        return self.__department

    @property
    def get_location(self):
        """
        Return location name
        """
        return self.__location

    @property
    def get_company_name(self):
        """
        Return company name
        """
        return self.__company_name

    @get_department.setter
    def get_department(self, new_department: str):
        """
        Can set new department only if it in all_departments list
        """
        all_departments = ['Research', 'Development', 'Engineering', 'Finance']

        if new_department in all_departments:
            self.__department = new_department
        else:
            raise Warning('You cannot set not approved department')

    @get_location.setter
    def get_location(self, new_location: str):
        """
        Allows to set company location if it in company_locations list
        """
        company_locations = ['China', 'EU', 'US']

        if new_location in company_locations:
            self.__location = new_location
        else:
            raise Warning('You cannot set not approved location')


if __name__ == '__main__':
    sony = Sony('Legal', 'US')
    print(sony.get_department)
    sony.get_location = 'EU'
