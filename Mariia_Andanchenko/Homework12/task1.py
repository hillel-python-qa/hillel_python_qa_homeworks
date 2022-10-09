import re


class Company:
    """
    A class Company contains the following information about a company:
    - the company name
    - age of the company
    - the value of the company
    - a list of company employees
    This class allows:
    - see the name of the company, its age and value
    - change the company name
    - add and remove an employee from the list
    - increase the age of the company
    - pay taxes
    - get an annual income
    """

    def __init__(self, name: str, age: int, cost: float, workers: list):
        self.__name = name
        self.__age = age
        self.__cost = cost
        self.__workers = workers

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        This function checks whether the new company name begins with an uppercase Latin letter,
        and if the condition is met - changes the company name
        """
        if re.search(r'^[A-Z]', new_name):
            self.__name = new_name
        else:
            raise Exception('Sorry, new name is not valid')

    @property
    def age(self):
        return self.__age

    @property
    def cost(self):
        return self.__cost

    def grow_up(self):
        """
        This function increase the age of the company
        """
        self.__age += 1

    def go_bankrupt(self):
        """
        This feature bankrupts the company - zeroing out the company's value and removing all employees
        """
        self.__cost = 0
        self.__workers.clear()

    def hire_workers(self, worker: dict):
        """
        This function adds a new employee to the company's employee list
        """
        self.__workers.append(worker)

    def lay_off_workers(self, worker_id: int):
        """
        This function deletes the specified employee ID from the list of company employees
        """
        self.__workers.pop(worker_id)

    def pay_taxes(self):
        """
        This function allows you to pay taxes
        """
        self.__cost -= 20.00

    def get_annual_income(self, annual_income: float):
        """
        This feature allows you to get an annual income
        """
        self.__cost += annual_income


if __name__ == '__main__':
    new_company = Company('Mio', 1, 100, [])
    new_company.name = 'Italy'
    print(new_company.name)
