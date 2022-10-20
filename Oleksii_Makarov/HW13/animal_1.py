from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, habitation: str, reproduction: str):
        self._habitation = habitation
        self._reproduction = reproduction

    @abstractmethod
    def _i_eat(self):
        pass

    @abstractmethod
    def _i_am_reproducing(self):
        pass
