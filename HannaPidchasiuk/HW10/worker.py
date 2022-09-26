from grade_enum import Grade
from department_enum import Department
from type_of_work_enum import TypeOfWork


class Worker:

    def __init__(self, first_name: str, last_name: str, salary: float, department: Department, grade: Grade,
                 type_of_work: TypeOfWork):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary
        self.__department = department
        self.__grade = grade
        self.__type_of_work = type_of_work

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
    def grade(self, new_value: Department):
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


if __name__ == "__main__":
    worker = Worker("name", "last_name", 12333, Department.QA_MANUAL, Grade.JUNIOR, TypeOfWork.OFFICE)
    worker.type_of_work = TypeOfWork.REMOTE
    worker.last_name = "kjf"
    print(worker.last_name, worker.type_of_work)
