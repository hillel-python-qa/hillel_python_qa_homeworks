from abc import ABC, abstractmethod


class ICamping:
    @abstractmethod
    def set_a_tent(self):
        print("Your tent is ready for resting")

    @abstractmethod
    def campfire(self):
        print("The heat is high, ready for the barbeque")

    @abstractmethod
    def singing(self):
        print("la la la la")
