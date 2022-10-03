class Company:
    def __init__(self, department: str, location: str, company_name):
        self.__department = department
        self.__location = location
        self.__company_name = company_name
        self.__number_of_max_workers = 50

    @property
    def department(self):
        """
        Return department name
        """
        return self.__department

    @property
    def location(self):
        """
        Return location name
        """
        return self.__location

    @property
    def company_name(self):
        """
        Return company name
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, new_name):
        self.__company_name = new_name

    @department.setter
    def department(self, new_department: str):
        """
        Can set new department only if it in all_departments list
        """
        all_departments = ['Research', 'Development', 'Engineering', 'Finance']

        if new_department in all_departments:
            self.__department = new_department
        elif new_department == '':
            raise Warning('You cannot set not approved department')
        else:
            raise Warning('You cannot set not approved department')

    @location.setter
    def location(self, new_location: str):
        """
        Allows to set company location
        """
        self.__location = new_location

    def chinese_workers(self):
        """
        For companies from China allows to have 100 workers.
        For other companies max number is 50
        """
        if self.__location == 'China':
            self.__number_of_max_workers = 100
        else:
            raise TypeError(f'Max workers for your company is {self.__number_of_max_workers}')

    def create_company_url(self):
        """
        Create URL based on company name
        """
        return f'{self.__company_name.lower().strip().replace(" ", "").replace("/", "-").replace("&", "-and-")}.com'

    def available_vacancies(self):
        """
        Notify that company has available positions in the company for current department
        """
        if self.__number_of_max_workers < (50 or 100):
            raise Warning(f'You have vacant positions in {self.__department} department!')

    def decrease_worker_number(self):

        if self.__number_of_max_workers == 0:
            raise Warning('You cannot set workers number lower than 0')
        else:
            self.__number_of_max_workers -= 1

    def increase_worker_number(self):
        if self.__location == 'China' and self.__number_of_max_workers < 100:
            self.__number_of_max_workers += 1
        elif self.__number_of_max_workers < 50:
            self.__number_of_max_workers += 1


if __name__ == '__main__':
    sony = Company('Legal', 'US', 'Sony')

