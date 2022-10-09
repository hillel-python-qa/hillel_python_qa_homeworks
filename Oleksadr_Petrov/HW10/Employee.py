from datetime import datetime


class Employee:

    def __init__(self, name: str, role: str, salary: float, department: str):
        self.__name = name
        self.__role = role
        self.__salary = salary
        self.__star_date = datetime.date()
        self.__department = department

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        """
        Name cannot be empty
        :param name
        """
        if name == '':
            raise Exception('Name cannot be empty')
        else:
            self.__name = name

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def name(self, role):
        """
             Role cannot be empty
             :param role
        """
        if role == '':
            raise Exception('Role cannot be empty')
        else:
            self.__role = role

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary):
        """
             Salary cannot be 0 or less
             :param salary
        """
        if salary < 0:
            raise Exception('Salary cannot 0 and less')
        else:
            self.__role = salary

    @property
    def start_date(self) -> datetime:
        return self.__star_date

    @property
    def department(self) -> float:
        return self.__department

    @department.setter
    def department(self, department):
        """
             department cannot be empty
             :param department
        """
        if department == '':
            raise Exception('Salary cannot 0 and less')
        else:
            self.__department = department





