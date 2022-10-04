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
        if new_name:
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
        if new_second_name:
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
            Set an employee's age to a new full number. Age must be an int
        """
        if type(new_age) == int:
            self.__age = new_age
        else:
            raise TypeError("new_age must be an int")

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
        if type(new_position) == str:
            self.__position = new_position
        else:
            raise TypeError("new_position must be a string")

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
        if type(new_salary) == float:
            self.__salary = new_salary
        else:
            raise TypeError("new_salary must be float")

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
        if type(new_experience) == float:
            if new_experience <= self.__experience:
                raise ValueError("New experience must be greater than old one")
            else:
                self.__experience = new_experience
        else:
            raise TypeError("setter accepts only float")

    def experience_adder(self, additional_exp: float):
        """
            Adds number to current experience. Must be a float.
        """
        if type(additional_exp) == float:
            if additional_exp > 0:
                self.__experience += additional_exp
            else:
                raise ValueError("additional experience must be positive")
        else:
            raise TypeError("Additional experience must be float")

    def fire(self):
        """
            Fire an employee from the position
        """
        self.__salary = 0
        self.__position = None


if __name__ == '__main__':
    Jane = Employee('Jane', 'Sanchez', 25, 'Manager', 2500, 5)
    Jane.experience_adder(4.0)
    print(Jane.experience)
    Jane.fire()
    print(Jane.position)
