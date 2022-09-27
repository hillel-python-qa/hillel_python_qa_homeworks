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

    @property
    def age(self):
        """
        The method is used to obtain worker's age
        """
        return self.__age

    @property
    def gender(self):
        """
        The method is used to obtain worker's gender
        """
        return self.__gender

    @property
    def position(self):
        """
        The method is used to obtain worker's position
        """
        return self.__position

    @property
    def company(self):
        """
        The method is used to obtain worker's company
        """
        return self.__company

    @property
    def salary(self):
        """
        The method is used to obtain worker's salary
        """
        return self.__salary


if __name__ == '__main__':
    john = Employees(name='John Wick', age=35, gender='male', position='hitman', company='Unknown', salary=4000)
    print(john.name, john.age, john.gender, john.position, john.company, john.salary)
