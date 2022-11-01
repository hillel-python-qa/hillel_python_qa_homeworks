from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def drink(self):
        pass

    @abstractmethod
    def go_walk(self):
        pass
