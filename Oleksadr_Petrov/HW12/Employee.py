class Employee:

    def __init__(self, grade: str, full_name: str, salary: float, position: str):
        """
        :param grade:
        :param full_name:
        :param salary:
        :param position:

        #hiding
        """
        self.__grade = grade
        self.__full_name = full_name
        self.__salary = salary
        self.__position = position

    # encapsulation
    @property
    def grade(self):
        return self.__grade

    # encapsulation
    @grade.setter
    def grade(self, grade):
        if grade == '':
            raise Exception('Wrong value for grade')
        self.__grade = grade

    # encapsulation
    @property
    def full_name(self):
        return self.__full_name

    # encapsulation
    @full_name.setter
    def full_name(self, full_name):
        if full_name == '':
            raise Exception('Wrong value for Full Name')
        self.__full_name = full_name

    # encapsulation
    @property
    def salary(self):
        return self.__salary

    # encapsulation
    @salary.setter
    def salary(self, salary):
        if salary <= 0:
            raise Exception('Wrong value for salary')
        self.__salary = salary

    # encapsulation
    @property
    def position(self):
        return self.__position

    # encapsulation
    @position.setter
    def position(self, position):
        if position == '':
            raise Exception('Wrong value for position')
        self.__position = position

    # polymorphism
    def work(self):
        print('Im work as Employee')
