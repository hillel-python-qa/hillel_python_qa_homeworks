from grade_enum import Grade
from department_enum import Department
from type_of_work_enum import TypeOfWork
from datetime import datetime


class Worker:

    def __init__(self, first_name: str, last_name: str, salary: float, department: Department, grade: Grade,
                 type_of_work: TypeOfWork, date_of_start: datetime):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary
        self.__department = department
        self.__grade = grade
        self.__type_of_work = type_of_work
        self.__date_of_start = date_of_start

    @property
    def first_name(self):
        """
            Returns first_name property of the worker.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, new_value: str):
        """
            Set new first_name property of the worker.
            Takes only 1 argument: new_value.
        """
        self.__first_name = new_value

    @property
    def last_name(self):
        """
            Returns last_name property of the worker.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, new_value: str):
        """
            Set new last_name property of the worker.
            Takes only 1 argument: new_value.
        """
        self.__last_name = new_value

    @property
    def salary(self):
        """
            Returns salary property of the worker.
        """
        return self.__salary

    @salary.setter
    def salary(self, new_value: int):
        """
            Set new salary property of the worker.
            Takes only 1 argument: new_value.
        """
        if new_value < 0:
            raise ValueError("Salary can't be less than zero.")
        else:
            self.__salary = new_value

    @property
    def department(self):
        """
            Returns department property of the worker.
        """
        return self.__department

    @department.setter
    def department(self, new_value: Department):
        """
            Set new department property of the worker.
            Takes only 1 argument: new_value.
        """
        self.__department = new_value

    @property
    def grade(self):
        """
            Returns grade property of the worker.
        """
        return self.__grade

    @grade.setter
    def grade(self, new_value: Grade):
        """
            Set new grade property of the worker.
            Takes only 1 argument: new_value.
        """
        self.__grade = new_value

    @property
    def type_of_work(self):
        """
            Returns type of work for worker.
        """
        return self.__type_of_work

    @type_of_work.setter
    def type_of_work(self, new_value: TypeOfWork):
        """
            Set new type of work for the worker.
            Takes only 1 argument: new_value.
        """
        self.__type_of_work = new_value

    @property
    def date_of_start(self):
        """
            Returns first working day date.
        """
        return self.__date_of_start

    @date_of_start.setter
    def date_of_start(self, new_value: datetime):
        """
            Set new first working day date.
            Takes only 1 argument: new_value.
        """
        self.__date_of_start = new_value

    def count_overtimes(self, overtime_hours: int, average_hours: float) -> float:
        """
            Function takes 2 arguments and count price for overtimes:
                - overtime_hours - amount of hours to pay for;
                - average_hours - average amount of working hours for current month
        """
        if not overtime_hours or not average_hours:
            raise ZeroDivisionError("Working hours/overtime hours can't be 0!")
        else:
            return round((self.__salary / average_hours * overtime_hours), 2)

    def count_working_period(self):
        """
            Counts period worker works in a company.
            If less than 1 year only month number will be returned.
            If less than 1 month - number of working days will be returned.
        """
        period = datetime.now() - self.__date_of_start
        years = period.days // 365
        months = (period.days % 365) // 31
        if months < 1:
            return period.days
        elif years < 1:
            return months
        else:
            return years, months

    def count_vacation_days(self):
        """
            Returns number of vacation days depending on working period for current year.
        """
        months = ((datetime.now() - self.__date_of_start).days % 365) // 30
        return months * 2


if __name__ == "__main__":
    worker = Worker("name", "last_name", 12333, Department.QA_MANUAL, Grade.JUNIOR,
                    TypeOfWork.OFFICE, datetime(2022, 8, 27))
    worker.type_of_work = TypeOfWork.REMOTE
    worker.last_name = "kjf"
    print(worker.count_working_period())
    print(worker.count_overtimes(12, 177))
    print(worker.count_vacation_days())
