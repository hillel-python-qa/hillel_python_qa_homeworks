import re
from abc import ABC, abstractmethod


class Human(ABC):
    # abstraction
    def __init__(self, first_name: str, second_name: str, age: int, gender: str):
        self._first_name = first_name
        self._second_name = second_name
        self._age = age
        self._gender = gender

    @abstractmethod
    def ageing(self):
        pass


class Employee(Human):
    def __init__(self, first_name, second_name, age, gender: str, position: str):
        # inheritance
        super().__init__(first_name, second_name, age, gender)
        # hiding
        self.__position = position

    @property
    def first_name(self):
        # encapsulation
        """
            Returns value of first_name
        """
        return self._first_name

    @first_name.setter
    def first_name(self, new_name):
        # encapsulation
        """
            Set's first_name value to new if new value is a filled string.
        """
        if re.search(r'\S', new_name):
            self._first_name = new_name
        else:
            raise ValueError("Name must be filled")

    @first_name.deleter
    def first_name(self):
        # encapsulation
        """
            Sets first_name value to none
        """
        self._first_name = None

    @property
    def second_name(self):
        # encapsulation
        """
            Returns value of second_name
        """
        return self._second_name

    @second_name.setter
    def second_name(self, new_name):
        # encapsulation
        """
            Set's second_name value to new if new value is a filled string.
        """
        if re.search(r'\S', new_name):
            self._second_name = new_name
        else:
            raise ValueError("Name must be filled")

    @second_name.deleter
    def second_name(self):
        # encapsulation
        """
            Sets second_name value to none
        """
        self._second_name = None

    @property
    def age(self):
        # encapsulation
        """
            Returns value of age
        """
        return self._age

    @age.setter
    def age(self, new_age):
        # encapsulation
        """
            Set's first_name value to new if new value is a positive int.
        """
        if type(new_age) is int and new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age must be a positive int")

    @property
    def gender(self):
        # encapsulation
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        # encapsulation
        """
            Sets gender value to new if new value is a filled string.
        """
        if re.search(r'\S', new_gender):
            self._gender = new_gender
        else:
            raise ValueError("Gender must be filled")

    @property
    def position(self):
        # encapsulation
        """
            Returns position value
        """
        return self.__position

    @position.setter
    def position(self, new_position):
        # encapsulation
        """
             Sets position value to new if new value is a filled string.
         """
        if re.search(r'\S', new_position):
            self._second_name = new_position
        else:
            raise ValueError("Position must be filled")

    @position.deleter
    def position(self):
        # encapsulation
        """
            Sets position value to None
        """
        self.__position = None

    @staticmethod
    def work():
        # it says this method may be static
        # Polymorphism
        print(f"I work like {__class__.__name__}")

    def ageing(self):
        # Abstraction
        self._age += 1


class Baby(Human):
    def __init__(self, first_name: str, second_name: str, age: int, gender: str):
        # Inheritance
        super().__init__(first_name, second_name, age, gender)

    @property
    def first_name(self):
        # encapsulation
        """
            Returns value of first_name
        """
        return self._first_name

    @first_name.setter
    def first_name(self, new_name):
        # encapsulation
        """
            Set's first_name value to new if new value is a filled string.
        """
        if re.search(r'\S', new_name):
            self._first_name = new_name
        else:
            raise ValueError("Name must be filled")

    @first_name.deleter
    def first_name(self):
        # encapsulation
        """
            Sets first_name value to none
        """
        self._first_name = None

    @property
    def second_name(self):
        # encapsulation
        """
            Returns value of second_name
        """
        return self._second_name

    @second_name.setter
    def second_name(self, new_name):
        # encapsulation
        """
            Set's second_name value to new if new value is a filled string.
        """
        if re.search(r'\S', new_name):
            self._second_name = new_name
        else:
            raise ValueError("Name must be filled")

    @second_name.deleter
    def second_name(self):
        # encapsulation
        """
            Sets second_name value to none
        """
        self._second_name = None

    @property
    def age(self):
        # encapsulation
        """
            Returns value of age
        """
        return self._age

    @age.setter
    def age(self, new_age):
        # encapsulation
        """
            Set's first_name value to new if new value is a positive int.
        """
        if type(new_age) is int and new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age must be a positive int")

    @property
    def gender(self):
        # encapsulation
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        # encapsulation
        """
            Sets gender value to new if new value is a filled string.
        """
        if re.search(r'\S', new_gender):
            self._gender = new_gender
        else:
            raise ValueError("Gender must be filled")

    def ageing(self):
        # Abstraction
        self._age += 1

    @staticmethod
    def work():
        # Polymorphism
        print(f"I don't work")


if __name__ == '__main__':
    human = Employee('Aleksey', 'Makarov', 23, 'Male', 'QA')
    human.work()
    human.ageing()
    print(human.age)
    baby = Baby('Aleksey', 'Makarov', 4, 'Male')
    baby.work()
    baby.ageing()
    print(baby.age)
