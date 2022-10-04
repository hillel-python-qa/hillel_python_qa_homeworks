from datetime import datetime
from dateutil.relativedelta import relativedelta


class Employee:
    def __init__(self, name: str, start_day: str, salary: float, position: str):
        self.__name = name
        self.__start_day = start_day
        self.__salary = salary
        self.__position = position
        self.__course_access = None

        if self.__position not in ['junior', 'Junior', 'middle', 'Middle', 'senior', 'Senior']:
            raise TypeError('Please set correct employee position')

    @property
    def name(self):
        """
        Return employee name
        """
        return self.__name

    @property
    def start_day(self):
        """
        Return date when employee was accepted
        """
        return datetime.strptime(self.__start_day, '%d.%m.%Y').date()

    @property
    def salary(self):
        """
        Return employee current salary
        """
        return self.__salary

    @property
    def position(self):
        """
        Return employee work position
        """
        return self.__position

    @name.setter
    def name(self, new_name):
        """
        Allows set new name to employee
        """
        if not new_name.strip():
            raise TypeError('You cannot set empty value')
        else:
            self.__name = new_name.strip()

    @salary.setter
    def salary(self, new_salary):
        """
        Allows set new salary to employee
        """
        if new_salary < 0:
            raise TypeError("You cannot set value below 0")
        else:
            self.__salary = new_salary

    @property
    def course_access(self):
        """
        Returns None if not call employee_access
        """
        return self.__course_access

    def employee_bonus(self):
        """
        Calculate how long employee is working and add a bonus to a salary
        """
        user_date = datetime.strptime(self.__start_day, '%d/%m/%Y').date()
        current_date = datetime.now().date()
        rdelta = relativedelta(current_date, user_date)

        if rdelta.years >= 2:
            self.__salary += 500.1
            return self.__salary

    def employee_access(self):
        """
        If employee position upper then junior than give access to a special course
        """
        if self.__position == ('Junior' or 'junior'):
            self.__course_access = False
        else:
            self.__course_access = True


if __name__ == '__main__':
    josh = Employee('Josh', '01/10/2020', 1200, 'middle')

    josh.salary = 0


