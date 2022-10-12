from abc import ABC, abstractmethod


class Parent(ABC):
    def __init__(self, name: str, gender: str, age: int):
        # Hiding
        self._name = name
        self._gender = gender
        self._age = age

        if self._age < 18:
            raise TypeError('Available only for 18+')

    def growing_up(self):
        self._age += 1

    # Abstraction
    @abstractmethod
    def feeding(self):
        pass

    # Polymorphism
    @abstractmethod
    def make_baby(self):
        pass
