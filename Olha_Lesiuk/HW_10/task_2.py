import datetime
from datetime import date


class Employees:

    """
    The init method or constructor
    """""
    def __init__(self, name: str, birth: datetime.date, gender: str, position: str, company: str, salary: int):
        """"
        Instance Variable
        """
        self.__name = name
        self.__birth = birth
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
        if name:
            self.__name = name
        else:
            raise ValueError("You should enter a name!")

    @property
    def get_age(self):
        today = date.today()
        age = today.year - self.__birth.year - ((today.month, today.day) < (self.__birth.month, self.__birth.day))
        return age

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
        if gender:
            self.__gender = gender
        else:
            raise ValueError("You should enter a gender!")

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
        if position:
            self.__position = position
        else:
            raise ValueError("Your should enter a position!")

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
        if company:
            self.__company = company
        else:
            raise ValueError("You should enter company name!")

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
        if salary:
            self.__salary = salary and salary > 0
        else:
            raise ValueError("You should enter valid amount of salary!")

    def raise_salary(self, amount: int):
        self.__salary = self.salary + amount


if __name__ == '__main__':
    john = Employees(name='John', birth=datetime.date(1988, 12, 2),
                     gender='male', position='qa', company='Hyfe', salary=200)
    print(john.name, john.gender, john.position, john.company, john.salary)
    print('John is {} years old'.format(john.get_age))
