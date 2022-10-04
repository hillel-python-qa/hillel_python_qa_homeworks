from datetime import datetime

from HannaPidchasiuk.HW10.department_enum import Department
from HannaPidchasiuk.HW10.grade_enum import Grade
from HannaPidchasiuk.HW10.type_of_work_enum import TypeOfWork
from HannaPidchasiuk.HW10.worker import Worker


# Inheritance
class QualityAssurance(Worker):
    def __init__(self, first_name: str, last_name: str, salary: float, department: Department, grade: Grade,
                 type_of_work: TypeOfWork, date_of_start: datetime, is_manual: bool):
        super().__init__(first_name, last_name, salary, department, grade, type_of_work, date_of_start)
        # Hiding
        self.__is_manual = is_manual

    # Encapsulation
    @property
    def is_manual(self):
        """
            Returns true if QA is manual, false if automation.
        """
        return self.__is_manual

    # Encapsulation
    @is_manual.setter
    def is_manual(self, new_value: bool):
        """
            Set new type of QA.
            Takes only 1 argument: new_value.
            If same value tried to be set - returns ValueError.
        """
        if new_value is not self.__is_manual:
            self.__is_manual = new_value
        else:
            raise ValueError("No changes to save!")

    # Polymorphism
    def count_overtimes(self, overtime_hours: int, average_hours: float) -> float:
        """
            Function takes 2 arguments and count price for overtimes:
                - overtime_hours - amount of hours to pay for;
                - average_hours - average amount of working hours for current month
            Adding extra coefficient special for QA_Automation.
        """
        if not overtime_hours or not average_hours:
            raise ZeroDivisionError("Working hours/overtime hours can't be 0!")
        elif not self.__is_manual:
            return round((self.__salary * 1.25 / average_hours * overtime_hours), 2)
        else:
            return round((self.__salary / average_hours * overtime_hours), 2)
