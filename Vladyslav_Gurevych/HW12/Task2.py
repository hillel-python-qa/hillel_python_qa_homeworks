class Employee:
    def __init__(self, first_name: str, second_name: str, age: int, departament: str, role: str, salary: int):
        self.__first_name = first_name.capitalize()
        self.__second_name = second_name.capitalize()
        self.__age = age
        self.__department = departament.upper()
        self.__role = role.capitalize()
        self.__salary = salary

    @property
    def first_name(self):
        """
            This function returns first name of the employee
        """
        return self.__name

    @first_name.setter
    def first_name(self, new_first_name: str):
        """
            This function changes first name of the employee
        """
        self.__first_name = new_first_name

    @first_name.deleter
    def first_name(self):
        """
            This function does not allow users to delete the first name of employee
        """
        pass

    @property
    def second_name(self):
        """
            This function returns second name of the employee
        """
        return self.__second_name

    @second_name.setter
    def surname(self, new_second_name: str):
        """
            This function changes second name of the employee
        """
        self.__second_name = new_second_name

    @surname.deleter
    def surname(self):
        """
            This function does not allow users to delete the second name of employee
        """
        pass

    @property
    def age(self):
        """
            This function returns age of employee
        """
        return self.__age

    def celebrate_birthday(self, new_age: int):
        """
            This function changes age of employee after his birthday
        """
        if new_age > self.age:
            self.__age = new_age
        else:
            raise TypeError('Employee can not get younger')

    @age.deleter
    def age(self):
        """
            This function does not allow users to delete age of employee
        """
        pass

    @property
    def department(self):
        """
            This function returns age of employee
        """
        return self.__department

    def move_to_another_department(self, new_department: str, new_role: str, new_salary: int):
        """
            This function changes departament when employee get a new position in a new departament
        """
        self.__department = new_department
        self.__role = new_role
        self.__salary = new_salary

    def fire_employee(self):
        """
            This function set value None when employee is fired
        """
        self.__department = None
        self.__role = None
        self.__salary = None

    @department.deleter
    def department(self):
        """
            This function does not allow users to delete the department of the employee
        """
        pass

    @property
    def role(self):
        """
            This function returns role of employee
        """
        return self.__role

    @role.setter
    def position(self, new_role: str):
        """
            This function changes role when employee get a new one
        """
        self.__role = new_role

    @role.deleter
    def role(self):
        """
            This function does not allow users to delete the role of the employee
        """
        pass

    @property
    def salary(self):
        """
            This function returns salary of employee
        """
        return self.__salary

    @salary.setter
    def salary(self, new_salary: int):
        """
            This function changes salary of employee
        """
        self.__salary = new_salary

    @salary.deleter
    def salary(self):
        """
            This function does not allow users to delete the salary of the employee
        """
        pass


if __name__ == '__main__':
    hwang = Employee('hwang', 'Kihun', 22, 'Developers', 'Middle Java developer', 2250)
    hwang.move_to_another_department('QA', 'Senior JS AQA', 3500)
    print(hwang.department, hwang.role, hwang.salary)
    hwang.fire_employee()
    print(hwang.department, hwang.role, hwang.salary)
    hwang.celebrate_birthday(23)
    print(hwang.age)
