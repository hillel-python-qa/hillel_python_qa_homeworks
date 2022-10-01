class Worker:
    """
    The Worker class contains the following information about the employee:
    - name
    - age
    - work experience
    - salary
    This class allows:
    - see the name and length of service of the employee
    - get a salary
    - do some work
    - take a vacation
    - get bonuses
    - get a salary increase
    - celebrate a birthday
    """

    def __init__(self, name: str, age: int, length_work: float, salary: float):
        self.__name = name
        self.__age = age
        self.__length_work = length_work
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def length_work(self):
        return self.__length_work

    def get_salary(self):
        """
        This function allows the employee to receive a salary
        """
        print(f'Співробітник {self.__name} отримав зарплатню у розмірі {self.__salary}грн')

    def working(self):
        """
        This function allows do some work
        """
        print(f'Співробітник {self.__name} виконує свої обов\'язки')

    def take_vacation(self, days: int):
        """
        This function allows the employee to take vacation. The number of vacation days is passed to the function
        """
        print(f'Співробітник {self.__name} взяв відпустку на {days} днів')

    def get_bonus(self, bonus: float):
        """
        This function issues a one-time payment to the employee. The payout amount is passed to the function
        """
        print(f'Співробітник {self.__name} отримав бонус у розмірі {bonus}грн')

    def add_salary(self, premium: float):
        """
        This function increases the employee's salary. The payout amount is passed to the function
        """
        self.__salary += premium

    def celebrate_birthday(self):
        """
        This function increases the employee's age and length of service by one unit,
        and also gives him a one-time payment in the amount of UAH 1000
        """
        print(f'Співробітник святкує день народження')
        self.__age += 1
        self.get_bonus(1000)
        self.__length_work += 1


itan: Worker = Worker('Itan', 37, 2.0, 30000)
itan.get_salary()
itan.add_salary(500)
itan.get_salary()
