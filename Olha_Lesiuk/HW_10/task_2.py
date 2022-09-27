class Employees:

    """
    The init method or constructor
    """""
    def __init__(self, name: str, age: int, gender: str, position: str, company: str, salary: int):
        """"
        Instance Variable
        """
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__position = position
        self.__company = company
        self.__salary = salary

    @property
    def name(self):
        """
        The method is used to obtain worker's name
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        The method is used in case of changing to the new name
        """
        self.__name = name

    @property
    def age(self):
        """
        The method is used to obtain worker's age
        """
        return self.__age

    @age.setter
    def age(self, age: int):
        """
        The method is used in case of reaching a certain age
        """
        if age < 18:
            raise ValueError("Sorry, your age is below eligibility criteria for this position")
        self.__age = age

    @property
    def gender(self):
        """
        The method is used to obtain worker's gender
        """
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        """
        The method is used in case of changing gender
        """
        self.__gender = gender

    @property
    def position(self):
        """
        The method is used to obtain worker's position
        """
        return self.__position

    @position.setter
    def position(self, position: str):
        """
        The method is used in case of promotion to the higher position
        """
        self.__position = position

    @property
    def company(self):
        """
        The method is used to obtain worker's company
        """
        return self.__company

    @company.setter
    def company(self, company: str):
        """
        The method is used in case of changing to the new company
        """
        self.__company = company

    @property
    def salary(self):
        """
        The method is used to obtain worker's salary
        """
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        """
        The method is used in case of changing a salary
        """
        self.__salary = salary


if __name__ == '__main__':
    john = Employees(name='John Wick', age=35, gender='male', position='hitman', company='Unknown', salary=4000)
    john.age = 15
    print(john.name, john.age, john.gender, john.position, john.company, john.salary)
