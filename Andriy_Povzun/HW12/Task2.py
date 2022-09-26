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
        """
        The method is used to obtain the name of the employee
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        The method is used to assign a new name. This attribute could be static,
        but theoretically the employee can change his name when he changes his passport
        """
        self.__name = new_name

    @name.deleter
    def name(self):
        """
        Deleter written so that users do not break the design of the class
        """
        pass

    @property
    def surname(self):
        """
        The method is used to obtain the surname of the employee
        """
        return self.__surname

    @surname.setter
    def surname(self, new_surname: str):
        """
        The method is used to assign a new surname. This attribute could be static,
        but theoretically the employee can change his surname when he changes his passport,
        or married
        """
        self.__surname = new_surname

    @surname.deleter
    def surname(self):
        """
        Deleter written so that users do not break the design of the class
        """
        pass

    @property
    def age(self):
        """
        The method is used to obtain the age of the employee
        """
        return self.__age

    def grow_up(self, ages: int):
        """
        The employee will become older by the number of years indicated in the function
        """
        self.__age += ages

    @age.deleter
    def age(self):
        """
        Deleter written so that users do not break the design of the class
        """
        pass

    @property
    def work_place(self):
        """
        The method is used to obtain the work place of the employee
        """
        return self.__work_place

    def change_work_place(self, new_work_place: str, new_position: str, new_salary: int):
        """
        The method is used to change the work of an employee.
        This function uses 3 attributes at once, because when changing jobs,
        position and salary almost never remain untouched
        """
        self.__work_place = new_work_place
        self.__position = new_position
        self.__salary = new_salary

    def dismiss_employee(self):
        """
        The method is used to fire an employee
        """
        self.__work_place = None
        self.__position = WITHOUT_WORK
        self.__salary = None

    @work_place.deleter
    def work_place(self):
        """
        Deleter written so that users do not break the design of the class
        """
        pass

    @property
    def position(self):
        """
        The method is used to obtain the position of the employee
        """
        return self.__position

    @position.setter
    def position(self, new_position: str):
        """
        The method is used to change the position of an employee in the current job
        """
        self.__position = new_position

    @position.deleter
    def position(self):
        """
        Deleter written so that users do not break the design of the class
        """
        pass

    @property
    def salary(self):
        """
        The method is used to obtain the salary of the employee
        """
        return self.__salary

    @salary.setter
    def salary(self, new_salary: int):
        """
        The method is used to change the employee's salary
        """
        self.__salary = new_salary

    @salary.deleter
    def salary(self):
        """
        Deleter written so that users do not break the design of the class
        """
        pass


if __name__ == '__main__':
    bob = Employee('Boby', 'Grin', 32, 'Raiffeisen Bank Aval', 'QA Engineer', 755)
    bob.change_work_place('SoftServe', 'QA Automation', 1200)
    print(bob.work_place, bob.position, bob.salary)
    bob.dismiss_employee()
    print(bob.work_place, bob.position, bob.salary)
