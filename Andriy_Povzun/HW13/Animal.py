from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_group: str, sub_group: str):
        self._animal_group = animal_group
        self._sub_group = sub_group

    @property
    def animal_group(self):
        return self._animal_group

    @property
    def sub_group(self):
        return self._sub_group

    @abstractmethod
    def _i_eat(self):
        ...

    @abstractmethod
    def _my_special(self):
        ...

    @abstractmethod
    def _i_live(self):
        pass
