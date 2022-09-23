class Worker:

    def __init__(self, first_name: str, last_name: str, salary: float, department: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary
        self.__department = department

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        self.__last_name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: int):
        self.__salary = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value: str):
        self.__department = value
