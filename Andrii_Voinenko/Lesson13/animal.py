from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, name: str, gender: str, health: str):
        self.__name = name
        self.__gender = gender
        self.__health = health
        self.__feeding = None

        if self.__health not in ['bad', 'normal', 'good']:
            raise TypeError('Set correct value for health: bad, normal or good')

    def creature_death(self):
        if self.__health == 'bad':
            return False
        else:
            return True

    def creature_mating(self):
        if self.__health == 'bad':
            print('Health of the creature is too bad for mating')
            self.__feeding = True
            return self.__feeding




