import re


class Employee:
    def __init__(self, first_name: str, second_name: str, age: int, position: str, salary: float, experience: float):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age
        self.__position = position
        self.__salary = salary
        self.__experience = experience

    @property
    def first_name(self):
        """
            Returns first name of employee
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, new_name):
        """
            Sets a new first name. Name should not be empty
        """
        if re.search(r'\S', new_name):
            self.__first_name = new_name
        else:
            raise ValueError("Name must not be empty")

    @property
    def second_name(self):
        """
            Returns second name of employee
        """
        return self.__second_name

    @second_name.setter
    def second_name(self, new_second_name):
        """
            Sets a new second name. Second name shouldn't be empty.
        """
        if re.search(r'\S', new_second_name):
            self.__second_name = new_second_name
        else:
            raise ValueError("Second name must not be empty")

    @property
    def age(self):
        """
            Returns age of employee in full years
        """
        return self.__age

    @age.setter
    def age(self, new_age):
        """
            Set an employee's age to a new full number. Age must be an int within limit of 18 years to 120 years.
        """
        if type(new_age) == int and new_age in range(18, 120):
            self.__age = new_age
        else:
            raise TypeError("new_age must be an int in range from 18 to 120")

    @property
    def position(self):
        """
            Returns a position of employee
        """
        return self.__position

    @position.setter
    def position(self, new_position):
        """
            Set a new position for employee. Position should be a string
        """
        if type(new_position) == str and re.search(r'\S', new_position):
            self.__position = new_position
        else:
            raise TypeError("new_position must be a filled string")

    @position.deleter
    def position(self):
        """
            Sets employee's position to None.
        """
        self.__position = None

    @property
    def salary(self):
        """
            Returns salary of employee in USD
        """
        return f'{self.__salary}$'

    @salary.setter
    def salary(self, new_salary):
        """
            Sets salary of the employee. Must be a float
        """
        if type(new_salary) == float and new_salary >= 0:
            self.__salary = new_salary
        else:
            raise TypeError("new_salary must be float above zero")

    @salary.deleter
    def salary(self):
        """
            Sets salary to None
        """
        self.__salary = None

    @property
    def experience(self):
        """
            Returns experience of the employee
        """
        return self.__experience

    @experience.setter
    def experience(self, new_experience):
        """
            Sets a new experience of the employee. Must be a Float
        """
        if type(new_experience) == float and new_experience >= 0:
            if new_experience >= (self.__age - 18):
                raise ValueError("Experience cannot be greater than (age - 18 years)")
            else:
                self.__experience = new_experience
        else:
            raise TypeError("setter accepts only numbers above zero")

    def fire(self):
        """
            Fire an employee from the position
        """
        print(f'{self.__first_name} {self.__second_name} is fired from {self.__position} position')
        self.__salary = 0
        self.__position = None

    def taxes(self):
        """
            Function check employee's position and adjust their salary according to tax
        """
        # I hate this part
        if self.__position == 'Manager':
            tax = self.__salary * 0.21
        elif self.__position == 'Engineer':
            tax = self.__salary * 0.25
        elif self.__position == 'Intern':
            tax = self.__salary * 0.13
        elif self.__position == 'CEO':
            tax = self.__salary * 0.3
        elif self.__position is None:
            tax = 0
        else:
            tax = self.__salary * 0.2
        self.__salary = self.__salary - tax
        print(f'{self.__first_name} {self.__second_name}\'s salary after tax of {tax} is {self.__salary}')

    def promote(self):
        if self.__position is not None:
            if self.__position == 'Intern':
                self.__position = 'Engineer'
            elif self.__position == 'Manager':
                self.__position = 'CEO'
            self.__salary = self.__salary * 2
            print(f'{self.__first_name}{self.__second_name} was promoted to {self.__position}'
                  f' with new salary of {self.__salary}')
        else:
            print(f'Cannot promote. {self.__first_name} has no position in company')


if __name__ == '__main__':
    Jane = Employee('Jane', 'Sanchez', 25, 'CEO', 2500, 5)
    print(Jane.experience)
    print(Jane.position)
    Jane.age = 19
    Jane.experience = 0.9
    print(Jane.age)
    # Jane.taxes()
    # Jane.fire()
    # Jane.taxes()
    Jane.promote()
    Jane.taxes()
