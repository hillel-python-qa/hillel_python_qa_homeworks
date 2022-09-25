WITHOUT_WORK = 'Unemployed'


class Employee:
    def __init__(self, name: str, surname: str, age: int, work_place: str, position: str, salary: int):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__work_place = work_place
        self.__position = position
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    """
    The method is used to obtain the name of the employee
    """

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    """
    The method is used to assign a new name. This attribute could be static, 
    but theoretically the employee can change his name when he changes his passport
    """

    @name.deleter
    def name(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def surname(self):
        return self.__surname

    """
    The method is used to obtain the surname of the employee
    """

    @surname.deleter
    def surname(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def age(self):
        return self.__age

    """
    The method is used to obtain the age of the employee
    """

    @age.deleter
    def age(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def work_place(self):
        return self.__work_place

    """
    The method is used to obtain the work place of the employee
    """

    def change_work_place(self, new_work_place: str, new_position: str, new_salary: int):
        self.__work_place = new_work_place
        self.__position = new_position
        self.__salary = new_salary
        return self

    """
    The method is used to change the work of an employee. 
    This function uses 3 attributes at once, because when changing jobs,
     position and salary almost never remain untouched
    """

    def dismiss_employee(self):
        self.__work_place = None
        self.__position = WITHOUT_WORK
        self.__salary = None

    """
    The method is used to fire an employee
    """

    @work_place.deleter
    def work_place(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def position(self):
        return self.__position

    """
    The method is used to obtain the position of the employee
    """

    @position.setter
    def position(self, new_position: str):
        self.__position = new_position

    """
    The method is used to change the position of an employee in the current job
    """

    @position.deleter
    def position(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """

    @property
    def salary(self):
        return self.__salary

    """
    The method is used to obtain the salary of the employee
    """

    @salary.setter
    def salary(self, new_salary: int):
        self.__salary = new_salary

    """
    The method is used to change the employee's salary
    """

    @salary.deleter
    def salary(self):
        pass

    """
    Deleter written so that users do not break the design of the class
    """


if __name__ == '__main__':
    bob = Employee('Boby', 'Grin', 32, 'Raiffeisen Bank Aval', 'QA Engineer', 755)
    bob.change_work_place('SoftServe', 'QA Automation', 1200)
    print(bob.work_place, bob.position, bob.salary)
    bob.dismiss_employee()
    print(bob.work_place, bob.position, bob.salary)
